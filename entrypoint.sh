#!/bin/sh

echo "init database"

echo "Waiting for postgres..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

echo "\nRun init.py\n"
python init.py

echo "\nRun Application.\n"
python app.py