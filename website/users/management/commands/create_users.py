from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from faker import Faker
from users.models import CustomUser
from unidecode import unidecode
from django.db import transaction
import time
import os
import threading


BATCH_SIZE = 100
NUM_THREADS = os.cpu_count()


class CreateUsersThread(threading.Thread):
    def __init__(self, fake, users_to_create, quantity):
        threading.Thread.__init__(self)
        self.fake = fake
        self.users_to_create = users_to_create
        self.quantity = quantity

    def run(self):
        for _ in range(self.quantity):
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()
            full_name = f"{first_name} {last_name}"
            username = f"{first_name[0].lower()}{last_name.lower()}"
            username = unidecode(username)
            pre_email = f"{first_name.lower()}.{last_name.lower()}"
            pre_email = unidecode(pre_email)
            email = f"{pre_email}@gmail.com"
            password = make_password("123")

            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                full_name=full_name,
                username=username,
                email=email,
                password=password
            )
            self.users_to_create.append(user)

            if len(self.users_to_create) >= BATCH_SIZE:
                with transaction.atomic():
                    CustomUser.objects.bulk_create(self.users_to_create, ignore_conflicts=True)
                self.users_to_create = []

        if self.users_to_create:
            with transaction.atomic():
                CustomUser.objects.bulk_create(self.users_to_create, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Create new users"

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='Number of users to create')

    def handle(self, *args, **kwargs):
        start_time = time.time()
        quantity = kwargs['quantity']
        fake = Faker('pl-PL')
        users_to_create = []

        threads = []
        for _ in range(NUM_THREADS):
            thread = CreateUsersThread(fake, users_to_create, quantity // NUM_THREADS)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        elapsed_time = time.time() - start_time
        print(f"{quantity} users created in {elapsed_time:.2f} sec")
