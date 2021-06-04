# -*- coding: utf-8 -*-
import json
from django.test import TestCase
from rest_framework.views import status
import httpretty
from apps.dogs import dogs_service

from apps.dogs.models import Dog


class TestDogsViews(TestCase):
    @httpretty.activate
    def test_get_dogs_returns_a_list(self):
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
                    },
                    {
                        "id": 1,
                        "name": "Welsh Springer Spaniel",
                        "bred_for": "Small rodent hunting, lapdog",
                        "breed_group": "Sporting",
                        "bred_for": "Small rodent hunting, lapdog",
                        "breed_group": "Toy",
                        "life_span": "10 - 12 years",
                        "temperament": "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving",
                        "origin": "Germany, France",
                    },
                ]
            ),
        )

        dogs_service.seed_dog()
        # make a get request to fetch dog data
        response = self.client.get("/api/dogs/list")
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @httpretty.activate
    def test_get_dogs_returns_allows_for_optional_filtering(self):
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
                        "life_span": "10 - 12 years",
                        "temperament": "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving",
                        "origin": "Germany, France",
                    },
                    {
                        "id": 1,
                        "name": "Welsh Springer Spaniel",
                        "bred_for": "Small rodent hunting, lapdog",
                        "breed_group": "Sporting",
                        "life_span": "10 - 12 years",
                        "temperament": "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving",
                        "origin": "Germany, France",
                    },
                ]
            ),
        )

        dogs_service.seed_dog()
        # make a get request to fetch dog data
        response = self.client.get(
            "/api/dogs/list?breed_group=Toy&&name=Affenpinscher&&bred_for=Small&&life_span=10&&temperament=Stubborn&&origin=Germany"
        )
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @httpretty.activate
    def test_get_dog_by_id(self):
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
                        "bred_for": "Small rodent hunting, lapdog",
                        "breed_group": "Toy",
                        "life_span": "10 - 12 years",
                        "temperament": "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving",
                        "origin": "Germany, France",
                    },
                    {
                        "id": 1,
                        "name": "Welsh Springer Spaniel",
                        "bred_for": "Small rodent hunting, lapdog",
                        "breed_group": "Sporting",
                        "bred_for": "Small rodent hunting, lapdog",
                        "life_span": "10 - 12 years",
                        "temperament": "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving",
                        "origin": "Germany, France",
                    },
                ]
            ),
        )

        dogs_service.seed_dog()
        response = self.client.get("/api/dogs/2/details/")
        self.assertEqual(response.data["id"], 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @httpretty.activate
    def test_get_dog_by_id_should_return_404_for_non_existent_id(self):
        response = self.client.get("/api/dogs/2/details/")
        self.assertFalse(response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
