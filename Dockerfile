FROM postgres:9.5

COPY ./db/init_database.sql /docker-entrypoint-initdb.d