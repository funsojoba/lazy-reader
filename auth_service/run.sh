#!/bin/sh

if [ -z ${LOG_LEVEL} ]; then
export LOG_LEVEL="debug"
fi

if [ -z ${HTTP_PORT} ]; then
export HTTP_PORT=":5003"
fi
if [ -z ${HTTP_WORKERS} ]; then
export HTTP_WORKERS=2
fi


export FLASK_APP=src.app:app
echo "Initializing DB..."

flask db init
flask db migrate -m "Initial migration"
flask db upgrade



status=$?
if [ $status -eq 0 ]; then
  echo "$(tput setaf 1)initiating flask app . . .$(tput sgr0)"
  gunicorn --workers $HTTP_WORKERS \
           --worker-class=gthread \
           --reload $FLASK_APP \
          -b $HTTP_PORT \
          --timeout 120 \
          --log-level $LOG_LEVEL \
          --log-file=-
else
  echo "$(tput setaf 1)Error starting flask . . .$(tput sgr0)"
fi
