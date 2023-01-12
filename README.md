#documentation for mini_django_v2

s## Documentation for `mini_django_v2`.



## cookie-cutter

Creates a skeleton of project (structure of project)


## shoppingpal.com

    - UPI
    - CART
    - RECOMMENDATION
    - 


## project structure


```markdown

mini_django_v2 (project-root)
    - venv
    - requirements.txt
    - manage.py
    - db.sqlite3 (database file)
    - mini_django_v2 (project-settings folder)
        - __init__.py
        - urls.py (global setting for urls)
        - wsgi.py (needed for deployment)
        - asgi.py  (needed for deployment)
        - settings.py (project level configs)
    - app1
        - __init__.py
        - admin.py (we register our data models here)
        - models.py (data-base DDL)
        - apps.py (application configuration)
        - tests.py (unit-tests)
        - views.py (to write business logic)
        - urls.py (app specific urls)
        - templates
            - app1
                - app1_landing_page.html
        - migrations (`makemigration` command adds data model changes here)
            - __init__.py
```

    


### NOTE

- In django project structure, wherever `manage.py` file is created is the project root.
- There is a directory matching with project root name under project root itself and that is for project level settings.
- default database used by django is `sqlite`


## Steps to create django project

- step 1: Create new directory
- step 2: Create new virtual environment under it
- step 3: activate venv and `pip install django`
- step 4: `django-admin startproject myproject`
- step 5: `python manage.py startapp app1`
- Step 6: Create model under `app1/models.py`
- Step 7: Register the model to `app1/admin.py`
- Step 8: Register app under `INSTALLED_APP` directive in `settings.py`
- Step 9: `python manage.py makemigrations` (To detect changes in data models)
- Step 10: `python manage.py migrate` (To apply DDL created in step 7)
- Step 11: Go to `http://127.0.0.1:8000/admin` and it will ask user-name and password
- Step 12: We have created data table for `AUTH` app but there are no entries. We create first user using `python manage.py createsuperuser`
- Step 13: `python manage.py runserver`

# `WSGI` vs `ASGI`

- Specifications used for deployment on `application server`.