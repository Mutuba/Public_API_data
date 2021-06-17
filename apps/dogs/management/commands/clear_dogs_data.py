from django.core.management.base import BaseCommand

from apps.dogs.dogs_service import clear_dogs_data


class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_dogs_data()
        print("completed")
