FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip3 install flask-httpauth
RUN pip3 install passlib
RUN pip3 install flask-iiif
RUN pip3 install couchdb
RUN pip3 install requests
RUN pip3 install numpy
RUN pip3 install opencv-python

ENV LISTEN_PORT 4000
EXPOSE 4000

COPY ./app /app
COPY ./nginx_ext.conf /etc/nginx/conf.d
