release: rm db.sqlite3;rm -r migrations;python manage.py makemigrations OroWebhook; python manage.py migrate
web: gunicorn JoanOro.wsgi --log-file -
