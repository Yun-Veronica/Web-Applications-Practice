# restarting nginx
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# restarting gunicorn
sudo /etc/init.d/gunicorn restart


#  gunicorn [OPTIONS] [WSGI_APP]
#  path to wsgi app looks like this: folder.file-without-extension:function_name
gunicorn --bind='0.0.0.0:8000' web.hello:wsgi_app
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test
gunicorn --bind='0.0.0.0:8080' web.ask.ask.wsgi:application
sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf web.ask.ask.wsgi:application

