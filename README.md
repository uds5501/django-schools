# Django School

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.0-brightgreen.svg)](https://djangoproject.com)

This is an school erp project forked from [django-schools](https://github.com/sibtc/django-multiple-user-types-example.git). In this Django app, teachers can create quizzes and students can sign up and take quizzes related to their interests.


## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/suhailvs/django-schools.git
```

### Install the requirements:

```bash
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
./manage.py makemigration
./manage.py migrate
./manage.py runserver
```
The project will be available at <http://127.0.0.1:8000>


## License

The source code is released under the [MIT License](https://github.com/suhailvs/django-schools/blob/master/LICENSE).
