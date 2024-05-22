from django.urls import path
from .views import concertListView

urlpatterns=[
    path("tickets/",concertListView)
]