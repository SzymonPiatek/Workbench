from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import CustomUser
import os


class Command(BaseCommand):
    help = "Add worker group to all users"

    def handle(self, *args, **kwargs):
        all_users = CustomUser.objects.all()
        worker_group = Group.objects.filter(name="worker").first()

        for user in all_users:
            user.groups.add(worker_group)
        self.stdout.write(self.style.SUCCESS(f"Worker group added to all users"))
