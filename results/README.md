# As follows:

django-admin startproject results  
python manage.py startapp active
python manage.py runserver

add active to INSTALLED_APPS in ./settings.py
create home.html in ./active/temaplates
add home function in ./active/views.py

make sure ./results/urls.py is like this:

from django.contrib import admin
from django.urls import path, re_path  # note re_path

from active import views

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns = [
    re_path(r'^$', views.home, name='home'),  # note re_path
]