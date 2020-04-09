# Deployment

For Production use, Zenetti is intended to run as an Docker container.

The Container `tiangolo/uwsgi-nginx-flask` Provides an NGINX-Server and Python with an preconfigured environment to run the flask app. 

## Environment

```
+ - - - - - - +               + - - - - - - - - +               + - - - - - - - - - +
|             |               |                 | (Container)   |                   |
|   CouchDB   | - - - - - - - |     Zenetti     | - - - - - - - |   Reverse Proxy   |
|             |               |                 |               |  (Routing, HTTPS, |
+ - - - - - - +               + - - - - - - - - +               |   Compression)    |
                                       |                        |                   |
                                       | Mounting Point         + - - - - - - - - - +
+ - - - - - - - - - +                  |
|                   |                  |
|  Data Directory   | - - - - - - - - - 
|                   |
+ - - - - - - - - - +


```

## Build Process

### Required Packages

flask

flask-httpauth

flask-iiif

passlib

couchDB

numpy

opencv-python

## Updates







