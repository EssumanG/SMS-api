#!/bin/bash

# Deactivate the current environment if any is active
if [ -n "$VIRTUAL_ENV" ]; then
    deactivate
    echo "Deactivated the current environment: $VIRTUAL_ENV"
else
    echo "No virtual environment is currently active."
fi

# Activate the environment
if [ -f "./env/Scripts/activate" ]; then
    source ./env/Scripts/activate
    echo "Activated the environment located at ./env/Scripts/activate."
else
    echo "The environment activation script was not found at ./env/Scripts/activate."
    exit 1
fi

# Run the server
if [ -f "manage.py" ]; then
    echo "Starting the server..."
    python manage.py runserver
else
    echo "manage.py not found in the current directory."
    exit 1
fi
