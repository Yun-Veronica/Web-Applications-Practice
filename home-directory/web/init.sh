sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# restarting gunicorn
sudo /etc/init.d/gunicorn restart
gunicorn --bind='0.0.0.0:8080' hello:wsgi_app


