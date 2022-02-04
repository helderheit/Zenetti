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

### CouchDB in Docker
**Important**: Zenetti is not Compatible with CouchDB 3.x a the moment.

> docker run -d --restart always -v path/to/local/storage:/opt/couchdb/data --name couchdb --net=host couchdb:2.3

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

In the project directory

> docker build -t zenetti .

> docker run -d --name zenetti1  -v path/to/local/storage:/app/webapp/data --net=host zenetti 



## Updates







