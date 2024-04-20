from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from faker import Faker
from users.models import CustomUser
from unidecode import unidecode
from django.db import transaction
import time


class Command(BaseCommand):
    help = "Create new basic users"

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='Number of users to create')

    @transaction.atomic
    def handle(self, *args, **kwargs):
        start_time = time.time()
        quantity = kwargs['quantity']
        fake = Faker('pl-PL')

        batch_size = 100
        users_to_create = []

        while len(users_to_create) < quantity:
            user_data = []
            for _ in range(quantity - len(users_to_create)):
                first_name = fake.first_name()
                last_name = fake.last_name()
                full_name = f"{first_name} {last_name}"
                username = f"{first_name[0].lower()}{last_name.lower()}"
                username = unidecode(username)
                pre_email = f"{first_name.lower()}.{last_name.lower()}"
                pre_email = unidecode(pre_email)
                email = f"{pre_email}@gmail.com"
                password = make_password("123")

                try:
                    CustomUser.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        full_name=full_name,
                        username=username,
                        email=email,
                        password=password
                    )
                except IntegrityError:
                    pass

                user_data.append(CustomUser(
                    first_name=first_name,
                    last_name=last_name,
                    full_name=full_name,
                    username=username,
                    email=email,
                    password=password
                ))

                if len(user_data) >= batch_size:
                    users_to_create.extend(user_data)
                    CustomUser.objects.bulk_create(user_data, ignore_conflicts=True)
                    user_data = []

            users_to_create.extend(user_data)
            CustomUser.objects.bulk_create(user_data, ignore_conflicts=True)

        elapsed_time = time.time() - start_time
        print(f"{quantity} użytkowników utworzono pomyślnie w ciągu {elapsed_time:.2f} sekund.")
