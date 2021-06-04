from django.core.management.base import BaseCommand

from apps.dogs.dogs_service import clear_data


class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_data()
        print("completed")
