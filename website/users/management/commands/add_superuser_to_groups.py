from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import CustomUser
import os
import time


class Command(BaseCommand):
    help = "Add all groups to superuser"

    def handle(self, *args, **kwargs):
        start_time = time.time()

        admin = CustomUser.objects.filter(username=os.environ.get("ADMIN_USERNAME")).first()
        all_groups = Group.objects.all()

        if admin:
            all_groups = Group.objects.all()
            for group in all_groups:
                admin.groups.add(group)
            elapsed_time = time.time() - start_time
            self.stdout.write(self.style.SUCCESS(
                f"Added groups to '{os.environ.get("ADMIN_USERNAME")}' in {elapsed_time:.2f} sec")
            )
        else:
            elapsed_time = time.time() - start_time
            self.stdout.write(self.style.ERROR(f"'{os.environ.get("ADMIN_USERNAME")}' not found in {elapsed_time:.2f} sec"))
