# -*- coding: utf-8 -*-
"""setting up system"""
import socket, os, json

print("This system will help you setting up Zenetti")
hostname = input("hostname (default: http://localhost:4000):")
if hostname =="":
    hostname = "http://localhost:4000"
master_username = input("master username:")
master_password = input("master password:")

print("please check your configuration an press enter to continue:")
print("host  "  + hostname)
print("master username is "  + master_username)
print("master password is "  + master_password)
input()
print("creating config dir...")
try:
    os.mkdir("app/config")
except:
    pass

config = {
    "host": hostname,
    "master_username": master_username,
    "master_password": master_password
}
print("writing app.conf...")
try:
    with open("app/config/app.conf", "w") as outfile:
        json.dump(config, outfile)
        outfile.close()
    print("Zenetti is now configured. You can now run the application and log in to create user accounts")
except Exception as e:
    print("ERROR, could not write configfile" + str(e))
