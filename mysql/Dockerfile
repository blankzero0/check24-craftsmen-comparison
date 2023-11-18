FROM mysql:latest

# Copy environment variable file
COPY mysql.env /tmp/

# Copy all SQL files
COPY *.sql /docker-entrypoint-initdb.d/

# Expose port
EXPOSE 3306
