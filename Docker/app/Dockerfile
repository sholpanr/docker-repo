FROM ubuntu:latest
RUN apt update
RUN apt install nginx -y
# RUN ???start service
ENV NAME=Aksholpan
VOLUME /var/www/html
WORKDIR /var/www/html
# RUN rm index.html
COPY index.html .
COPY team1.png .
CMD ["nginx", "-g", "daemon off;"]
SHELL ["/bin/bash", "-c"]

# USER aksholpan
STOPSIGNAL SIGSTOP