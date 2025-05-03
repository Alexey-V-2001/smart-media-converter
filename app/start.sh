#!/bin/bash

if [[ $1 != "-f" ]]; then
    echo "[Installing requirements]"
    ./install_requirements.sh

    echo "[Initializing project]"
    ./initialize.sh
fi

if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "Activating virtual environment..."
    source ./venv/bin/activate
fi

echo "Launching the development server..."
cd media_converter
python manage.py runserver 0.0.0.0:8000

deactivate