# Administration



## Add User

> **[POST]** api/1.0/users

Requires:

- username
- name
- password
- admin
- change_password

*Status Codes:*

- **200** *Added user*
- **409** *Could not add user*
- **422** *Missing field*
- **403** *Access denied*

## Edit User

> **[PUT]** api/1.0/users

Requires:

- username
- name
- password
- admin
- change_password

*Status Codes:*

- **200** *Updated user*
- **409** *Could not update user*
- **422** *Missing field*
- **403** *Access denied*

## Remove User

> **[DELETE]** api/1.0/users/USERNAME

*Status Codes:*

- **200** *Removed user*
- **409** *Could not remove user*
- **403** *Access denied*

## Get Users

> **[GET]** api/1.0/users

Returns a list of users containing:

- username
- name
- admin
- master
- change_password

*Status Codes:*

- **200** 
- **409** *Could not get users*
- **403** *Access denied*

## Get User

> **[GET]** api/1.0/users/USERNAME

Returns:

- username
- name
- admin
- master
- change_password

*Status Codes:*

- **200** 
- **409** *Could not get user*
- **403** *Access denied*

