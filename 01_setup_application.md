# Create a web application in Django

## Install Django
Django python module can be installed with pip
```bash
python -m pip install Django
```
## Project and Applications
* A Django project is a collection of applications

## Create a project
* Run the following command to create a Django project
```bash
django-admin startproject DjangoTraining .
```
* It will create a directory structure like the following
```bash
manage.py
DjangoTraining/
    __init__.py
    settings.py
    urls.py
    asgi.py
    wsgi.py
```
* The folder created with the project name contains the code and configuration to manage the project and its applications


## Run the project
* Open a command line in the project folder and run the following command
```bash
python manage.py runserver
```

* To run on a different port and hostname, use the following command
```bash
python manage.py runserver 0.0.0.0:80
```

## Create an application in project
* Create an application in the project using the following command
```bash
python manage.py startapp MainSite
```
* It will create an application folder as shown below
```bash
MainSite/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

## Register the application
* The newly created application should be registered in the `settings.py` file of the main application
* Example snippet from `settings.py` is shown below

```py
# DjangoTraining/settings.py
# ...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'MainSite',
]
#...
```

## URLs and views
* A URL pattern can be configured to dispatch the request to a view
* The view is a function that can take in the HTTP request and send the response 

## Include the new application URLs in project
* Include the URLs of the new application in the project in `urls.py` file of the project folder as shown below
```py
# DjangoTraining/urls.py
# ...
from django.urls import include, path

urlpatterns = [
    #...
    path('mainsite/', include("MainSite.urls") )
    
]
```

## Create URLs file in new application
* Map a view function to each url pattern of the application in the `urls.py` file of the application
```py
# MainSite/urls.py
#...
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
]
```

## Create a view function to render content
* A view function can take in the HTTP request and send the response
* The response can be plain text, data rendered in a jinja HTML template, JSON etc.

```py
# MainSite/views.py
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context={"name":"John"}
    return render(request, 'index.html.j2', context)
    # return render(request, 'App2/index.html.j2', context)
    # return HttpResponse("hello World")
```

## Templates to render views in application
* Template files should be present in the `templates` folder of the application
* Variabled passed from the view function can be rendered in HTML using jinja templating as shown in the below example

```html
<!--MainSite/templates/index.html.j2-->
<h1>Main Site</h1>
<h2>Hello {{name}}!!!</h2>
```

## Access the web application page
* The web page can be accessed at `http://localhost:8000/mainsite` 