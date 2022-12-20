# Django-with-GeoDjango-Setup

## Steps to Setup Django with GeoDjango

- Install the necessary dependencies:

    ```bash
    pip install django
    pip install psycopg2
    pip install geos
    pip install gdal
    pip install proj
    ```

- Add the django.contrib.gis module to the INSTALLED_APPS list in your Django settings.py file:

    ```bash
    INSTALLED_APPS = [
        ...
        'django.contrib.gis',
    ]
    ```

- Set the DATABASES setting in your settings.py file to use a spatial database. For example, to use PostGIS with the psycopg2 adapter:

    ```bash
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'mydatabase',
            'USER': 'mydatabaseuser',
            'PASSWORD': 'mypassword',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    ```