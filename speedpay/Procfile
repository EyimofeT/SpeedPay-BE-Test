release: python manage.py makemigrations --no-input
release: python3 manage.py migrate --run-syncdb --no-input 

web: gunicorn speedpay.wsgi
