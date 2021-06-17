import requests
from .models import Dog
from .serializers import DogsSerializer


def get_dogs_data():
    endpoint = "https://api.thedogapi.com/v1/breeds/"
    response = requests.get(endpoint).json()

    return response


def seed_dogs_data():
    for dog in get_dogs_data():
        dog["initial_id"] = dog.get("id", None)
        serializer = DogsSerializer(data=dog)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


def clear_dogs_data():
    Dog.objects.all().delete()
