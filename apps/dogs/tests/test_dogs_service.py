# -*- coding: utf-8 -*-
import json
from django.test import TestCase
import httpretty
from apps.dogs import dogs_service

from apps.dogs.models import Dog


class TestDogsService(TestCase):
    @httpretty.activate
    def test_seed_dog(self):
        # mock for fetching dogs from DogsAPI
        httpretty.register_uri(
            httpretty.GET,
            "https://api.thedogapi.com/v1/breeds/",
            body=json.dumps(
                [
                    {
                        "id": 1,
                        "name": "Affenpinscher",
                        "bred_for": "Small rodent hunting, lapdog",
                        "breed_group": "Toy",
                        "bred_for": "Small rodent hunting, lapdog",
                        "breed_group": "Toy",
                        "life_span": "10 - 12 years",
                        "temperament": "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving",
                        "origin": "Germany, France",
                    }
                ]
            ),
        )

        dogs_service.seed_dog()
        dogs = Dog.objects.all()
        self.assertEqual(len(dogs), 1)
