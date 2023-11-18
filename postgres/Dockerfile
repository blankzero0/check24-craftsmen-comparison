FROM postgres:14.9

# Copy environment variable file
COPY postgres.env /tmp/

# Copy all SQL files
COPY *.sql /docker-entrypoint-initdb.d/

# Set environment variables from file
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
