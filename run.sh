celery -A src.jobs worker -l info -c 1 \
& flower -A src.jobs --address=0.0.0.0 --port=5555 --basic_auth=floweruser:ewogICAgImlk \
& gunicorn src.app:app  -b 0.0.0.0:8080 -t 120 --capture-output --access-logfile - --error-logfile - --log-level info
