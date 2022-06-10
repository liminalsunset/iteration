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
