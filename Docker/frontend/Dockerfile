ARG VAR=latest
FROM nginx:${VAR}

VOLUME /index


# RUN apk update && \
#     apk add bash
#RUN apk update && apk add nginx 
RUN apt install atop -y
RUN rm /usr/share/nginx/html/index.html
# COPY index.html /usr/share/nginx/
# COPY team1.png /usr/share/nginx/

# RUN chmod +x custom-web.sh
# RUN ./custom-web.sh



# #RUN mkdir /test

# WORKDIR should be after copy 
# WORKDIR /test
# # COPY --from=class:1.2 /test/hello.txt .
# VOLUME /data
# #CMD while running container
# #CMD can be overwritten by commands during the running stage
# #ENTRYPOINT commands cannot be changed
ENV name=Aksholpan

#RUN while building stage
#RUN chmod 777 docker-entrypoint.sh
#ENTRYPOINT before CMD
#ENTRYPOINT cannot be changed and running stage (sourcing and executing) (cmd of container without ch)
ENTRYPOINT ["/docker-entrypoint.d/docker-entrypoint.sh"]
#RUN service nginx start
# CMD ["service", "nginx", "start"]
# CMD ["nginx", "-g", "daemon off;"]
EXPOSE 80 
# HEALTHCHECK --interval=10m --timeout=3s \
#   CMD curl -f http://localhost/ || exit 1

  #SHELL - default, if want bash specify while exec
  #graceful stop - waits until all process stop - SIGTERM - default
  #STOPSIGNAL SIGSTOP - will pause main process  but not container
  #STOPSIGNAL SIGCON - continiue process
  #STOPSIGNAL SIGKILL - forcefully kill

#RUN useradd User_name
#USER USERNAME (2 options of adding a user)
#USER 1000 (to specify and user ID)
# 

# SHELL ["/bin/bash", "-c"]
# # RUN sudo adduser Aksholpan
# # USER Aksholpan
# STOPSIGNAL SIGSTOP






