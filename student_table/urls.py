from django.urls import path
from . import views

urlpatterns = [
    path('', views.st_table, name="st_table"),

]
