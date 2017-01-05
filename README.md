This is HashedIn's standard template for Django Projects.

## Features
* Django 1.9.x
* Whitenoise for static files
* Configuration via environment variables using dj_database_url and dj_email_url
* Sane logging defaults
* Using pip-tools to pin requirements.in / requirements.txt
* MySQL or Postgres for database
* Optional support for Celery
* Optional support for TravisCI and CircleCI
* Optional support for Heroku and AWS Elastic Beanstalk
* Optional support for NewRelic and LogEntries
* Optional support for Django Rest Framework


## Quick Start

Create a directory for your repository and cd into it
```bash
cd puremagic && cd $_
```

Create a virtualenv 
```bash
virtualenv venv
```

Install [cookiecutter](https://github.com/audreyr/cookiecutter):
```bash
pip install cookiecutter
```

Run cookiecutter. To prevent an extra directory, keep the repository name same as the directory you created above
```bash
cookiecutter https://github.com/hashedin/django-project-template -f -o ../
```

Upgrade pip, if necessary
```bash
pip install --upgrade pip
```

Install requirements.txt
```bash
pip install -r requirements.txt
```

Run pip-sync to uninstall cookicutter and any other extra dependencies
```bash
pip-sync
```

Commit the source code to git
```bash
git init .
git add -A 
git commit -m "Initial Commit using django-project-template"
```

At this point, your Django project is ready.


