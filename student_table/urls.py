from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path('register/', views.register, name="register"),
    path("loginhandle/",views.loginhandle, name="loginhandle"),
    path("loginhandle/logouthandle/",views.logouthandle, name="logouthandle"),
]
