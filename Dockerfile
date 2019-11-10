#Dockerfile
# Use ultima version de la imagen postgres image as the base
FROM postgres:11.5

COPY /sql /docker-entrypoint-initdb.d

RUN chmod +x /docker-entrypoint-initdb.d/base.sql
