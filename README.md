# Django School

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2-brightgreen.svg)](https://djangoproject.com)
[![CircleCI](https://circleci.com/gh/suhailvs/django-schools.svg?style=svg)](https://circleci.com/gh/suhailvs/django-schools)

This is an school erp project forked from [django-schools](https://github.com/sibtc/django-multiple-user-types-example.git).


## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/suhailvs/django-schools
```

Create Virtual Env and Install the requirements:

```bash
cd django-schools
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

### Create the database:

#### You might need to install postgresql:

```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql

ALTER USER postgres WITH PASSWORD 'root';
create database schools;
```
#### then migrate:

```bash
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```
The project will be available at <http://127.0.0.1:8000>

## Initialization

### Load Sample Data

#### Load Fixtures

For loading full fixtures read `schools/fixtures/README.md` **or** you can load few datas by `./manage.py loaddata sampledata.json`

#### Create Teacher 

+ Create a Teacher Account
+ Create super user `./manage.py createsuperuser`
+ Login as Superuser and give `Staff status` to teacher user & create an `AcademicYear`

## Deployment


Install Apache:

	$ apt-get update
	$ apt-get install python3-pip apache2 libapache2-mod-wsgi-py3

+ Change dir: `$ cd /var/www/`
+ Clone the repo: `$ git clone https://github.com/suhailvs/django-schools`
+ Change dir: `$ cd django-schools`

Create virtual and install django:

	$ pip3 install virtualenv
	$ virtualenv env
	$ source ./env/bin/activate
	$ pip install -r requirements.txt


Edit apache config :

	$ vi /etc/apache2/sites-available/djangoschool.conf

	Listen 8001
	<VirtualHost *:8001>
	    ServerName school.suhail.pw
	    WSGIDaemonProcess djangoschoolapp python-home=/var/www/django-schools/env python-path=/var/www/django-schools/django_school
	    WSGIProcessGroup djangoschoolapp
	    WSGIScriptAlias / /var/www/django-schools/django_school/django_school/wsgi.py
	    ErrorLog /var/www/django-schools/error.log
	    CustomLog /var/www/django-schools/access.log combined
	</VirtualHost>

restart apache: 

	$ a2ensite djangoschool.conf
	$ service apache2 reload
	
## License

The source code is released under the [MIT License](https://github.com/suhailvs/django-schools/blob/master/LICENSE).
