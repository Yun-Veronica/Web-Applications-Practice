#MySQL starting commands file

sudo /etc/init.d/mysql start
mysql -uroot -e "create database qadb;"
mysql -uroot -e "create user 'box'@'localhost' identified by '1234';"
mysql -uroot -e "grant all privileges on qadb.* to 'box'@'localhost' with grant option;"

~/web/ask/manage.py makemigrations qa
~/web/ask/manage.py migrate
