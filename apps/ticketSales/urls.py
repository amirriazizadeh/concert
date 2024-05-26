from django.urls import path
from .views import concertListView,concertDetails,timesInfo,locationsViews,concertEditView

urlpatterns=[
    path("",concertListView,name="home"),
    # path("locations/",listOfLocations,name="locatoins"),
    path("locations/",locationsViews.as_view(),name="locatoins"),
    path("details/<int:concertId>",concertDetails,name="details"),
    path("sans/",timesInfo,name="sans"),
    path("edit/<int:concert_id>",concertEditView,name="editPage"),
]