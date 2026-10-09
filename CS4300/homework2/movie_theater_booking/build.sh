#!/usr/bin/env bash

# Stop the build immediately if a command fails.
set -o errexit

# Install the Python dependencies listed in requirements.txt.
pip install -r requirements.txt

# Gather Django static files for production.
python manage.py collectstatic --no-input

# Apply database migrations.
python manage.py migrate