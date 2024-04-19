from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from faker import Faker
from users.models import CustomUser


class Command(BaseCommand):
    help = "Create new basic users"

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='Number of users to create')

    def handle(self, *args, **kwargs):
        quantity = kwargs['quantity']
        fake = Faker()
        i = 0

        while i != quantity:
            first_name = fake.first_name()
            last_name = fake.last_name()
            full_name = f"{first_name} {last_name}"
            username = f"{first_name[0].lower()}{last_name.lower()}"
            email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
            password = "123"

            if CustomUser.objects.filter(username=username).exists() or CustomUser.objects.filter(email=email).exists():
                self.stdout.write(self.style.ERROR('User with this username or email already exists.'))
            else:
                new_user = CustomUser.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    full_name=full_name,
                    username=username,
                    email=email,
                    password=make_password(password)
                )

                self.stdout.write(self.style.SUCCESS(f'User {i+1} - "{username}" created successfully.'))
                i += 1
