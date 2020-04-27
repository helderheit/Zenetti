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



### Docker Container

>docker build -t zenetti .

> docker run -d --name zenetti1 -p 4000:4000 -p 5984:5984 -v c:/data:/app/webapp/data --net=host zenetti 

## Updates







