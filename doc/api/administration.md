# Administration

> modules/api/administration.py

## User object

```json
{
    "username": [String], 	// unique username
    "name": [String], 		//displayed name of the user
    "password": [String],   //hashed password
    "admin": [Boolean],		
    "change_password": [Boolean]	//if this is true, the user is forced to change the password on login
}
```

## Add User

> **[POST]** api/1.0/users

### Required fields

```json
{
    "username": [String],
    "name": [String],
    "password": [String],
    "admin": [Boolean],
    "change_password": [Boolean]
}
```

### Status Codes

- **200** *Added user*
- **409** *Could not add user*
- **422** *Missing field*
- **401** *Access denied*

### Access

- admin users

## Edit User

> **[PUT]** api/1.0/users

### Required fields

```json
{
    "username": [String],
    "name": [String],
    "password": [String],
    "admin": [Boolean],
    "change_password": [Boolean]
}
```

### Status Codes

- **200** *Updated user*
- **409** *Could not update user*
- **422** *Missing field*
- **401** *Access denied*

### Access

- admin users
- users can get change their own account information

### Notes

If `password` is an empty string, the old password will not be updated

## Remove User

> **[DELETE]** api/1.0/users/`username`

### Status Codes

- **200** *Removed user*
- **409** *Could not remove user*
- **401** *Access denied*

### Access

- admin users

## Get Users

> **[GET]** api/1.0/users

### Returns

 a list of user objects

### Status Codes

- **200** 
- **409** *Could not get users*
- **401** *Access denied*

### Access

- admin user

## Get User

> **[GET]** api/1.0/users/`username`

### Returns

 a user object

### Status Codes

- **200** 
- **409** *Could not get user*
- **401** *Access denied*

### Access

- admin users
- users can get their own account information

