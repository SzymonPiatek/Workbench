from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import CustomUser
import os
import time


class Command(BaseCommand):
    help = "Add worker group to all users"

    def handle(self, *args, **kwargs):
        start_time = time.time()

        all_users = CustomUser.objects.all()
        worker_group = Group.objects.filter(name="worker").first()

        for user in all_users:
            user.groups.add(worker_group)

        elapsed_time = time.time() - start_time
        self.stdout.write(self.style.SUCCESS(f"Groups added to users in {elapsed_time:.2f} sec"))
