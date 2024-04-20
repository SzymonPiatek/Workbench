from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.hashers import make_password
from users.models import CustomUser
import os


class Command(BaseCommand):
    help = "Create test startup"

    def handle(self, *args, **kwargs):
        call_command("migrate")
        self.create_superuser()
        call_command("runserver")

    def create_superuser(self):
        admin_username = os.environ.get("ADMIN_USERNAME")
        admin_email = os.environ.get("ADMIN_EMAIL")
        admin_password = os.environ.get("ADMIN_PASSWORD")

        if not CustomUser.objects.filter(username=admin_username).exists():
            admin = CustomUser.objects.create_superuser(username=admin_username, email=admin_email,
                                                        password=admin_password)
            admin.save()
        else:
            self.stdout.write(self.style.ERROR(f"User with username '{admin_username}' already exists"))
