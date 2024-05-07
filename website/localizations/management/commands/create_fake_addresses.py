from django.core.management.base import BaseCommand
from django.db.models import Max
from localizations.models import Address
from faker import Faker
import random
import time


class Command(BaseCommand):
    help = "Create new address"

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='Number of addresses to create')

    def handle(self, *args, **kwargs):
        self.start_time = time.time()

        quantity = kwargs["quantity"]
        self.create_addresses(quantity)

    def create_addresses(self, quantity):
        i = 0
        max_id = Address.objects.aggregate(max_id=Max('id'))['max_id']
        if max_id:
            max_id = int(max_id)
        else:
            max_id = 0
        fake = Faker('pl-PL')

        voivodeships = [
            "dolnośląskie", "kujawsko-pomorskie", "lubelskie", "lubuskie", "łódzkie",
            "małopolskie", "mazowieckie", "opolskie", "podkarpackie", "podlaskie",
            "pomorskie", "śląskie", "świętokrzyskie", "warmińsko-mazurskie", "wielkopolskie", "zachodniopomorskie"
        ]

        while i != quantity:
            polish_adress = fake.postcode()

            city = fake.city()
            name = f"Oddział {city} nr {max_id + 1}"
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
                max_id += 1

        elapsed_time = time.time() - self.start_time
        self.stdout.write(self.style.SUCCESS(f'{i} Address created in {elapsed_time:.2f} sec'))
