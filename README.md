[![Build Status](https://travis-ci.com/Mutuba/Public_API_data.svg?branch=master)](https://travis-ci.com/Mutuba/Public_API_data)

# Tell me about Dogs API

An API with handy information about lovely dogs bacause very dog is a lovely dog.


## Vision

Create a datastore for data about dogs

---

## API Spec

The preferred JSON object to be returned by the API should be structured as follows:

### Dogs

```source-json
        {
            "id": 1,
            "initial_id": 1,
            "slug": "affenpinscher",
            "name": "Affenpinscher",
            "bred_for": "Small rodent hunting, lapdog",
            "breed_group": "Toy",
            "weight": {
                "metric": "3 - 6",
                "imperial": "6 - 13"
            },
            "height": {
                "metric": "23 - 29",
                "imperial": "9 - 11.5"
            },
            "image": {
                "id": "BJa4kxc4X",
                "url": "https://cdn2.thedogapi.com/images/BJa4kxc4X.jpg",
                "width": 1600,
                "height": 1199
            },
            "origin": "Germany, France",
            "reference_image_id": "BJa4kxc4X",
            "life_span": "10 - 12 years",
            "temperament": "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving"
        }
```

### Multiple Dogs
```source-json
{
    "count": 172,
    "next": "http://publicapidataapp.herokuapp.com/api/dogs/list?limit=10&offset=10",
    "previous": null,
    "results": [
        {
            "id": 1,
            "initial_id": 1,
            "slug": "affenpinscher",
            "name": "Affenpinscher",
            "bred_for": "Small rodent hunting, lapdog",
            "breed_group": "Toy",
            "weight": {
                "metric": "3 - 6",
                "imperial": "6 - 13"
            },
            "height": {
                "metric": "23 - 29",
                "imperial": "9 - 11.5"
            },
            "image": {
                "id": "BJa4kxc4X",
                "url": "https://cdn2.thedogapi.com/images/BJa4kxc4X.jpg",
                "width": 1600,
                "height": 1199
            },
            "origin": "Germany, France",
            "reference_image_id": "BJa4kxc4X",
            "life_span": "10 - 12 years",
            "temperament": "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving"
        },

        {
            "id": 10,
            "initial_id": 10,
            "slug": "american-bulldog",
            "name": "American Bulldog",
            "bred_for": null,
            "breed_group": "Working",
            "weight": {
                "metric": "27 - 54",
                "imperial": "60 - 120"
            },
            "height": {
                "metric": "56 - 69",
                "imperial": "22 - 27"
            },
            "image": {
                "id": "pk1AAdloG",
                "url": "https://cdn2.thedogapi.com/images/pk1AAdloG.jpg",
                "width": 1669,
                "height": 1377
            },
            "origin": null,
            "reference_image_id": "pk1AAdloG",
            "life_span": "10 - 12 years",
            "temperament": "Friendly, Assertive, Energetic, Loyal, Gentle, Confident, Dominant"
        }
    ]
}
```

### Other status codes:

404 for Not found requests, when a resource can't be found to fulfill the request


Endpoints:
----------

### List Dogs

`GET /api/dogs/list`

Returns dogs globally by default, provide `name`, `slug`, `bred_for`, `origin`, `weight`, `height`, `life_span` or `breed_group` query parameter to filter results

Query Parameters:

Filter by name:

`?name=American Bulldog`

Filter by origin:

`?origin=Germany, France`

Filter by life_span:

`?life_span=10 - 12 years`

Limit number of dogs (default is 20):

`?limit=20`

Offset/skip number of dogs (default is 0):

`?offset=0`


### Get a single Dog

`GET /api/dogs/:id/details`

Returns a single dog matching id in the param or 404 if the a dog with the id does not exist



### Application set up

The application uses Python 3.8 and Django 3. 

To set the application, clone the repo `git@github.com:Mutuba/Public_API_data.git` using SSH.

cd into `Public_API_data`

You can optionally run the application with `Docker` but first making sure you have docker installed on your machine.

Run `docker-compose up --build` to start the application by optionally building if it is not build yet, then starting all dependant services as per `docker-compose.yml` file.

To run application tests, execute `docker-compose run web python manage.py test`

The application has been hosted on Heroku here https://publicapidataapp.herokuapp.com/

### Credit

The API's initial data source is https://thedogapi.com/ Many thanks for such an awesome free service.
