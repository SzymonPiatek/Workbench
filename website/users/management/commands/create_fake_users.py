from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
import requests
import os
from users.models import CustomUser


class Command(BaseCommand):
    help = "Create new basic users"

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='Number of users to create')

    def handle(self, *args, **kwargs):
        quantity = kwargs['quantity']

        def generate_users_data(quantity):
            url = f"https://randommer.io/api/Name?nameType=fullname&quantity={quantity}"
            headers = {
                "X-Api-Key": os.environ.get("RANDOMMER_API_KEY")
            }

            try:
                response = requests.get(url, headers=headers)
                data = response.json()
                return data
            except requests.RequestException as e:
                print(e)
                return None

        def generate_users(users_data):
            i = 1
            for user_data in users_data:
                first_name, last_name = user_data.split()
                full_name = f"{first_name} {last_name}"
                username = f"{first_name[0].lower()}{last_name.lower()}"
                email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
                password = "123"

                if CustomUser.objects.filter(username=username).exists() or CustomUser.objects.filter(
                        email=email).exists():
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

                    self.stdout.write(self.style.SUCCESS(f'User {i} - "{username}" created successfully.'))
                    i += 1
        generate_users(generate_users_data(quantity))
