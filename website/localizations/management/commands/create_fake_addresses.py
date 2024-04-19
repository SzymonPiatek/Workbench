from django.core.management.base import BaseCommand
from localizations.models import Address
from faker import Faker
import random


class Command(BaseCommand):
    help = "Create new address"

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='Number of addresses to create')

    def handle(self, *args, **kwargs):
        quantity = kwargs["quantity"]
        i = 0
        fake = Faker('pl-PL')

        voivodeships = [
            "dolnośląskie", "kujawsko-pomorskie", "lubelskie", "lubuskie", "łódzkie",
            "małopolskie", "mazowieckie", "opolskie", "podkarpackie", "podlaskie",
            "pomorskie", "śląskie", "świętokrzyskie", "warmińsko-mazurskie", "wielkopolskie", "zachodniopomorskie"
        ]

        while i != quantity:
            polish_adress = fake.postcode()

            name = f"Address {random.randint(1, 100000)}"
            city = fake.city()
            street = fake.street_name()
            house_number = random.randint(1, 99)
            apartment_number = random.randint(1, 99)
            zip_code = fake.postcode()
            zip_code_city = city
            voivodeship = random.choice(voivodeships)
            country = "Polska"

            address = Address.objects.filter(name=name)

            if address:
                pass
            else:
                new_address = Address.objects.create(
                    name=name,
                    city=city,
                    street=street,
                    house_number=house_number,
                    apartment_number=apartment_number,
                    zip_code=zip_code,
                    zip_code_city=zip_code_city,
                    voivodeship=voivodeship,
                    country=country
                )

                i += 1

                self.stdout.write(self.style.SUCCESS(f'Address created successfully.'))
