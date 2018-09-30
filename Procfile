release: python manage.py migrate; python manage.py collectstatic; python manage.py init_demo
web: gunicorn demo_store.wsgi
