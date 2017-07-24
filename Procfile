release: rm -rf OroWebhook/migrations; rm db.sqlite3;python manage.py makemigrations OroWebhook ; python manage.py migrate
web: gunicorn JoanOro.wsgi --log-file -
