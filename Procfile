release: python manage.py makemigrations OroWebhook && python manage.py migrate --no-input
web: gunicorn JoanOro.wsgi --log-file -
