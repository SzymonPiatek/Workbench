from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from faker import Faker
from users.models import CustomUser
from unidecode import unidecode
from django.db import transaction


class Command(BaseCommand):
    help = "Create new basic users"

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='Number of users to create')

    @transaction.atomic
    def handle(self, *args, **kwargs):
        quantity = kwargs['quantity']
        fake = Faker('pl-PL')

        users_to_create = []
        existing_usernames = set(CustomUser.objects.values_list('username', flat=True))
        existing_emails = set(CustomUser.objects.values_list('email', flat=True))

        for i in range(quantity):
            first_name = fake.first_name()
            last_name = fake.last_name()
            full_name = f"{first_name} {last_name}"
            username = f"{first_name[0].lower()}{last_name.lower()}"
            username = unidecode(username)
            pre_email = f"{first_name.lower()}.{last_name.lower()}"
            pre_email = unidecode(pre_email)
            email = f"{pre_email}@gmail.com"
            password = make_password("123")

            if username not in existing_usernames and email not in existing_emails:
                users_to_create.append(CustomUser(
                    first_name=first_name,
                    last_name=last_name,
                    full_name=full_name,
                    username=username,
                    email=email,
                    password=password
                ))

                existing_usernames.add(username)
                existing_emails.add(email)

                print(i+1)

        print("User data generated")
        CustomUser.objects.bulk_create(users_to_create)
        print("User created")

        self.stdout.write(self.style.SUCCESS(f'{len(users_to_create)} users created successfully.'))
