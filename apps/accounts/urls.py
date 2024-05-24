from django.urls import path
from .views import loginView,logoutView,profileView

urlpatterns=[
    path("login/",loginView,name="login"),
    path("logout/",logoutView,name="logout"),
    path("profile/",profileView,name="profile"),
]