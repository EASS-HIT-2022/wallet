FROM mysql
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=users
COPY ./db /docker-entrypoint-initdb.d

EXPOSE 3306