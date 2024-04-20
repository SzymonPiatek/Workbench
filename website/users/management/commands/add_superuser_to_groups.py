from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import CustomUser
import os


class Command(BaseCommand):
    help = "Add all groups to superuser"

    def handle(self, *args, **kwargs):
        admin = CustomUser.objects.filter(username=os.environ.get("ADMIN_USERNAME")).first()
        all_groups = Group.objects.all()

        if admin:
            all_groups = Group.objects.all()
            for group in all_groups:
                admin.groups.add(group)
            self.stdout.write(self.style.SUCCESS(f"Added groups to user '{os.environ.get("ADMIN_USERNAME")}'"))
        else:
            self.stdout.write(self.style.ERROR(f"'{os.environ.get("ADMIN_USERNAME")}' user not found"))
