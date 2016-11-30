# {{cookiecutter.github_repository_name}}
# Introduction

Check out the project's [documentation](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}/) on github.

# Prerequisites
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

# Developer Guide

### Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```

Migrate, create a superuser, and run the server:
```bash
python manage.py migrate
python manage.py makemigrations {{cookiecutter.project_name}}
python manage.py createsuperuser
python manage.py runserver
```
### Setting up Environment Variables
- Edit the environment variables in **'.env.template'** file and then **RENAME** the file to **'.env'**

NOTE: This file has already been added to .gitignore, hence it will not be pushed to your repository.
While deployment or using CI tools like travis or circle-ci, you have to take care of setting the environment variables seperately.
### Database setup
This project uses dj-database-url library to setup databases. Use the  **DATABASE_URL** environment variable to configure your Django application. set this environment variable with the complete database url.
For more info: https://github.com/kennethreitz/dj-database-url

### Email server setup
This project uses dj-email-url library to setup email servers.
Provide your smtp server url in the **EMAIL_URL** environment variable.
For more info: https://github.com/migonzalvar/dj-email-url

### Static files
There's a 'static' directory configured already inside the project that is to be used to keep satic JavaScript, CSS, etc files to be used in templates.
### Test Cases
Some test cases have been included in the authentication/test directory.
Use the following command to run test cases in all apps.

```bash
python manage.py test
```

### Travis-CI
If Travis is setup, then use the **.travis.yml** file in the project root directory to configure travis settings, setting up test environment for travis etc.
For more info on travis, https://travis-ci.org/

## Circle-CI
If Circle-CI is setup, then it takes most of the settings from the project itself, but still there is a circle.yml file included at the project root for configuration.
for more info, https://circleci.com/docs/language-python/




