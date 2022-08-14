from django.contrib import admin
from django.urls import path, re_path


from active import views

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
]