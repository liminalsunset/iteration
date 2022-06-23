From the terminal:

1. Create a blank repo on Github
2. Make a directory for project
3. CD into directory
4. python3 -m venv env_name
5. source env_name/bin/activate

after you've created and activated your venv:

6. python3 -m pip install Django

It might be suggested you update pip here, if you'd like to you can:

python3 -m pip install --upgradepip

7. django-admin startproject project_name

cd into your project

8. python3 manage.py runserver

** You have 80,000 unapplied migrations

9. python3 manage.py migrate

10. Find a .gitignore

11. code .

12. In VS Code terminal once you open your project:

    - start the venv here by cd .. up to the root directory (where the venv is located) and type source env_name/bin/activate and then cd back into your project folder.

    - it should change to (env_name) -> project_name in the terminal

13. add the .gitignore at the same directory level as manage.py <=== !

    (I will probably add a link to a .gitignore)

    read the documentation on .gitignore
    https://git-scm.com/docs/gitignore

IMPORTANT!!:

Set up an ENV:

13. make sure your .gitignore ignores .env

14. make a .env file (at he same directory level as manage.py and your .gitignore)

15. Cut your secret key from settings.py (in project directory) and paste it in your .env 

16. Where your security key was in settings.py, replace that with (this is case sensitive, you're probably already aware but just in case):

from decouple import config

SECRET_KEY = config(“SECRET_KEY”)

17. Then in your terminal run:

pip install python-decouple
pip freeze > requirements.txt (I would google this further, but basically it seems to just keep track of your dependencies)

(here is a great site about this/python decouple: https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)


18. git init
19. git add .
20. git commit -m "first commit"
21. git branch -M main
22. git remote add origin .. (past your git remote origin address)

start app

In root directory:

23. python3 manage.py startapp myapp

In settings.py:

24. update INSTALLED_APPS --
    add 'myapp.apps.MyappConfig'

    * the django projects folder holds manage.py and the other module that includes settings.py
    * adding it to the settings.py under INSTALLED_APPS tells your project of its existence

--
    python3 manage.py startapp myapp

__

aside: Django MTV architecture: https://towardsdatascience.com/working-structure-of-django-mtv-architecture-a741c8c64082

