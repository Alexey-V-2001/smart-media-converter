BACK_DIR=$(pwd)

echo "Activating virtual environment..."
source ./venv/bin/activate

cd ./media_converter

echo "Applying migrations..."
python manage.py migrate

echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
User.objects.filter(username='$DJANGO_SUPERUSER_NAME').exists() or \
User.objects.create_superuser('$DJANGO_SUPERUSER_NAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASS')" | python manage.py shell

echo "Deactivating virtual environment..."
deactivate

cd $BACK_DIR