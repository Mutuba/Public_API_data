from django.core.management.base import BaseCommand

from apps.dogs.dogs_service import seed_dog


class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_dog()
        print("completed")
