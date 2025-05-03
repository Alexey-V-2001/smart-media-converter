if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "Creating virtual environment..."
    python -m venv venv

    echo "Activating..."
    source venv/bin/activate
fi

echo "Installing python-packages..."
pip install --no-cache-dir -r requirements.txt

echo "Deactivating..."
deactivate