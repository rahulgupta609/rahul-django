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

    filenames = ["ebsetenv.py"]
    for filename in filenames:
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


if __name__ == "__main__":
    perform_post_gen_action()
