# users and administration
from modules.api import api
from modules.database import database

def add_user(username, name, password, admin=False, change_password=False):
    """add a user-account to the database,return True on success

        Arguments:
        username -- username
        name -- the users name
        password -- password for the account
        admin -- if true, account gets admin-access
        change_password -- if true, user must change password on next login

    """
    try:
        user = api.User()
        user.hash_password(password)
        database.server[database.USER_DB_NAME][username] = {"username": username, "name": name, "password": user.password_hash,
                                     "admin": admin, "master": False, "change_password": change_password}
        print("Added user " + username + " to database")
        return True
    except Exception as e:
        print("Could not add user " + username + ": " + str(e))
        return False


def remove_user(username):
    """remove a user-account from the database,return True on success

        Arguments:
            username -- username
    """
    try:
        del database.server[database.USER_DB_NAME][username]
        print("Removed user " + username + " from database")
        return True
    except Exception as e:
        print("Could not remove user " + username + ": " + str(e))
        return False
    pass


def update_user(username, name, password, admin=False, change_password=False):
    """change name, password admin-access and change_password of a user

        Arguments:
        username -- username
        name -- the users name
        password -- password for the account, if password is empty string, password is not changed
        admin -- if true, account gets admin-access
        change_password -- if true, user must change password on next login
    """
    try:
        data = database.server[database.USER_DB_NAME][username]
        if password != "":
            user = api.User()
            user.hash_password(password)
            data["password"] = user.password_hash
        data["name"] = name
        data["admin"] = admin
        data["change_password"] = change_password
        database.server[database.USER_DB_NAME][username] = data
        print("Updated user " + username)
        return True
    except Exception as e:
        print("Could not update user " + username + ": " + str(e))
        return False


def get_user(username):
    """get a user from the database, return a User Object, returns None if user is not found"""
    try:
        data = database.server[database.USER_DB_NAME][username]
        name = data["name"]
        password = data["password"]
        admin = data["admin"]
        master = data["master"]
        change_password = data["change_password"]

        user = api.User(username=username, name=name, password_hash=password, admin=admin, master=master,
                    change_password=change_password)
        return user

    except Exception as e:
        print("Could not get user " + username + ": " + str(e))
        return None


def get_users():
    """get a list of users from the database, return a list of dicts"""
    try:
        user_list = []
        for user in database.server[database.USER_DB_NAME]:
            data = database.server[database.USER_DB_NAME][user]
            del data["password"]
            del data["_id"]
            del data["_rev"]
            user_list.append(data)
        return user_list

    except Exception as e:
        print("Could not get users: " + str(e))
        return None
