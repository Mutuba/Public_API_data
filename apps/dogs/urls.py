from rest_framework import routers
from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (
    DogsListView,
    DogRetrieveView,
)

router = DefaultRouter(trailing_slash=True)


app_name = "dogs"

urlpatterns = [
    path("list", DogsListView.as_view(), name="fetch_dogs"),
    path("<int:id>/details/", DogRetrieveView.as_view(), name="dog_details"),
]
