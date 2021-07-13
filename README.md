# About
This is a backend of application build with django framework

## Clone
```bash
$ git clone https://github.com/sipkyjayaputra/backend_django.git
```

## Installation Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Requirement
```bash
pip install -r requirements.txt
```

## Create Database
```
msyql -u root -p
create database article
quit
```

## Migrate Database
```bash
python manage.py makemigrations
python manage.py migrate
```

## Create Super User
```bash
python manage.py createsuperuser
```

## Usage
```bash
python manage.py runserver
```

