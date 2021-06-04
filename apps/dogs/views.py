from rest_framework import viewsets
from rest_framework.views import status
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework.pagination import LimitOffsetPagination

from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny

from .serializers import DogsSerializer
from .models import Dog


class DogsFilter(filters.FilterSet):

    breed_group = filters.CharFilter(method="filter_dog_breed_group")
    name = filters.CharFilter(method="filter_dogs_name")
    bred_for = filters.CharFilter(method="filter_by_bred_for")
    life_span = filters.CharFilter(method="filter_dog_life_span")

    temperament = filters.CharFilter(method="filter_dog_temperament")

    slug = filters.CharFilter(method="filter_dog_slug")

    height_metric = filters.CharFilter(method="filter_dog_height_metric")

    weight_metric = filters.CharFilter(method="filter_dog_weight_metric")

    class Meta:
        model = Dog
        fields = [
            "breed_group",
            "name",
            "bred_for",
            "life_span",
            "temperament",
            "slug",
            "height_metric",
            "weight_metric",
        ]

    def filter_dogs_name(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

    def filter_by_bred_for(self, queryset, name, value):
        return queryset.filter(bred_for__icontains=value)

    def filter_dog_life_span(self, queryset, name, value):
        return queryset.filter(life_span__icontains=value)

    def filter_dog_breed_group(self, queryset, name, value):

        return queryset.filter(breed_group__icontains=value)

    def filter_dog_temperament(self, queryset, name, value):
        return queryset.filter(temperament__contains=value)

    def filter_dog_slug(self, queryset, name, value):
        return queryset.filter(slug__icontains=value)

    def filter_dog_height_metric(self, queryset, name, value):
        return queryset.filter(height__metric=value)

    def filter_dog_weight_metric(self, queryset, name, value):
        return queryset.filter(weight__metric=value)


def schema_serializer_class(serializer_class, **kwargs):
    """A decorator to set a serializer class in detail or list method of ViewSets
    making it possible to extract the right serializer to generate the proper documentation
    """

    def decorator(func):
        func.schema_serializer_class = serializer_class
        func.kwargs = kwargs
        return func

    return decorator


class DogsListView(ListAPIView):

    """get: Return a list of all the existing dogs.
    Filters will be applied based on passed filter params
    """

    serializer_class = DogsSerializer
    filterset_class = DogsFilter
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = Dog.objects.all()
        return queryset


class DogRetrieveView(RetrieveAPIView):
    """Retrive a dog instance"""

    serializer_class = DogsSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get Dog by ID",
        operation_id="get_dog_by_id",
        responses={200: DogsSerializer},
    )
    def get(self, request, id=None):

        try:
            dog = Dog.objects.get(pk=id)
        except Dog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DogsSerializer(dog)
        return Response(serializer.data)
