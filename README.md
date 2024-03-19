
## gunucorn is can be run as a standalone process from the terminal (venv)
### command
``` bash
gunicorn -c conf/gunicorn_config.py myserver.wsgi:application
```

Gunicorn is not set up as a systemd service on your system. Instead,  appears to be running as standalone processes invoked directly from the command line within your virtual environment.

## or even better : make is a service in systemd : 



If you want to manage Gunicorn as a service using systemd: you can create a systemd service unit file to define how Gunicorn should be started, stopped, and managed by the system. Here's a basic example of how you can create a systemd service unit file for Gunicorn:

1- Create a new systemd service unit file for Gunicorn:

``` bash
sudo nano /etc/systemd/system/gunicorn.service
```
2-Add the following content to the file:

``` bash
[Unit]
Description=Gunicorn service for My Django Application
After=network.target

[Service]
User=ilyasss
Group=ilyasss
WorkingDirectory=/home/ilyasss/Desktop/z_programs/z_django_cloud/gunicorn_nginx_
Environment="PATH=/home/ilyasss/Desktop/z_programs/z_django_cloudgunicorn_nginx_/venv/bin"
ExecStart=/home/ilyasss/Desktop/z_programs/z_django_cloud/gunicorn_nginx_/venv/bin/gunicorn -c conf/gunicorn_config.py myserver.wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target

```
3- Save and close the file (in nano, you can do this by pressing Ctrl + X, then Y, and finally Enter).

4- Reload systemd to read the newly created service unit file:

``` bash
sudo systemctl daemon-reload
Start the Gunicorn service:

sudo systemctl start gunicorn
```
Enable the Gunicorn service to start on boot:

```
```bash
sudo systemctl enable gunicorn

```
Now you can manage Gunicorn using systemd commands like :
```bash
 systemctl start gunicorn,
  systemctl stop gunicorn,
   systemctl restart gunicorn, 
    systemctl status gunicorn.
    journalctl -u gunicorn

```

# run after every change :

## sudo  systemctl restart gunicorn
## sudo  systemctl restart nginx

