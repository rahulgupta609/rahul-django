# ACTIONS TO BE DONE AFTER THE PROJECT IS COMPLETED.
import os
import shutil

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def remove_heroku_files():
    """
    Removes files needed for heroku
    """
    filenames = ["Procfile", "runtime.txt"]
    for filename in filenames:
        file_name = os.path.join(PROJECT_DIRECTORY, filename)
        remove_file(file_name)


def remove_elasticbeanstalk():
    """
    Removes elastic beanstalk components
    """
    docs_dir_location = os.path.join(PROJECT_DIRECTORY, '.ebextensions')
    if os.path.exists(docs_dir_location):
        shutil.rmtree(docs_dir_location)

    filename = "ebsetenv.py"
    remove_file(os.path.join(
        PROJECT_DIRECTORY, filename
    ))


def remove_travis_ci():
    """
    Removes travis-ci yml file
    """
    filename = ".travis.yml"
    remove_file(os.path.join(
        PROJECT_DIRECTORY, filename
    ))


def remove_newrelic():
    """
    Removes Newrelic config file
    """
    filename = "{{cookiecutter.project_name}}/newrelic.ini"
    remove_file(os.path.join(
        PROJECT_DIRECTORY, filename
    ))


def remove_circle_ci():
    """
    Removes circle-ci yml file
    """
    filename = "circle.yml"
    remove_file(os.path.join(
        PROJECT_DIRECTORY, filename
    ))


def remove_celery():
    """
    Removes celery file
    """
    filename = "{{cookiecutter.project_name}}/celery.py"
    remove_file(os.path.join(
        PROJECT_DIRECTORY, filename
    ))


def perform_post_gen_action():
    """
    Performs actions needed after a Django project has been created.
    """
    # Removes heroku files
    if '{{ cookiecutter.use_heroku }}'.lower() != 'y':
        remove_heroku_files()

    # Removes Elastic Beanstalk files
    if '{{ cookiecutter.use_elasticbeanstalk }}'.lower() != 'y':
        remove_elasticbeanstalk()

    # Removes travis-ci files
    if '{{ cookiecutter.use_travis_ci }}'.lower() != 'y':
        remove_travis_ci()

    # Removes travis-ci files
    if '{{ cookiecutter.use_circle_ci }}'.lower() != 'y':
        remove_circle_ci()

    # Removes newrelic files
    if '{{ cookiecutter.use_newrelic }}'.lower() != 'y':
        remove_newrelic()

    # Removes celery file if not required
    if '{{ cookiecutter.use_celery }}'.lower() != 'y':
        remove_celery()


if __name__ == "__main__":
    perform_post_gen_action()
