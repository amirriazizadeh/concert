from django.urls import path
from .views import concertListView,listOfLocations,concertDetails,timesInfo

urlpatterns=[
    path("",concertListView,name="home"),
    path("locations/",listOfLocations,name="locatoins"),
    path("details/<int:concertId>",concertDetails,name="details"),
    path("sans/",timesInfo,name="sans"),
]