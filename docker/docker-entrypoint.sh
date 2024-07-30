#!/bin/bash

set -eo pipefail

wait_for_db() {
    max_retries=30
    retry_interval=5

    for ((i = 0; i < max_retries; i++)); do
        if </dev/tcp/${POSTGRES_HOST:-db}/5432; then
            echo "Database is available."
            return 0 # Database is available, exit successfully
        fi
        echo "Database is not yet available. Retrying in ${retry_interval} seconds..."
        sleep ${retry_interval}
    done

    echo "Timed out waiting for the database to become available."
    exit 1 # Exit with an error code
}

wait_for_obj_storage() {
    max_retries=30
    retry_interval=5

    for ((i = 0; i < max_retries; i++)); do
        if curl --silent -I ${MINIO_ENDPOINT:-http://minio:9000} >/dev/null; then
            echo "MINIO is available."
            return 0 # MINIO is available, exit successfully
        fi
        echo "MINIO is not yet available. Retrying in ${retry_interval} seconds..."
        sleep ${retry_interval}
    done

    echo "Timed out waiting for MINIO to become available."
    exit 1 # Exit with an error code
}

# Start wait in background with tmp log files
wait_for_db
if [[ ${OBJECT_STORAGE} == "MINIO" ]]; then
    wait_for_obj_storage
fi

python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput

exec "$@"
