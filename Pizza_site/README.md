# Pizza_site
simple Django pizza site (Python courses exam project)

Usage:

1. Create in a root directory file myEnvVal.py:

        import os

        def setVar():
            os.environ['EMAIL_HOST_USER'] = 'Your_email@gmail.com'
            os.environ['EMAIL_HOST_PASSWORD'] = 'your_password'

2. Create a virtual environment:
in a project folder:

        $ virtualenv venv
        $ source venv/bin/activate
        $ pip install -r requirements.txt

3. Run the project with command: 
        ./manage.py runserver
