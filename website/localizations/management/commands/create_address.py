from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "Create new address"

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='Number of addresses to create')

    def handle(self, *args, **kwargs):
        quantity = kwargs["quantity"]
        fake = Faker('pl-PL')

        for i in range(quantity):
            print(fake.first_name())

        self.stdout.write(self.style.SUCCESS(f'Address created successfully.'))