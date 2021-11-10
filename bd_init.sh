#MySQL starting commands file

sudo /etc/init.d/mysql start
mysql -uroot -e "create database qadb;"
mysql -uroot -e "create user 'box'@'localhost' identified by '1234';"
mysql -uroot -e "grant all privileges on qadb.* to 'box'@'localhost' with grant option;"

python3 manage.py makemigrations qa
python3 manage.py migrate
