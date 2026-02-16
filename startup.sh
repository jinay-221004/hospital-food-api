#!/bin/bash

apt-get update
apt-get install -y unixodbc-dev

gunicorn --bind=0.0.0.0 --timeout 600 app:app
