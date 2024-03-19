# gunicorn.conf


command='/home/ilyasss/Desktop/z_programs/z_django_cloud/gunicorn_nginx_/venv/bin/gunicorn'
pythonpath='/home/ilyasss/Desktop/z_programs/z_django_cloud/gunicorn_nginx_/myserver/'

# The address and port on which your application will run
bind = "127.0.0.1:8000"

# The number of worker processes (adjust according to your system's capabilities)
workers = 3

# The WSGI module and application
module = 'myserver.wsgi:application'