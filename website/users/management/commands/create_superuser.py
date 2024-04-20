from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from users.models import CustomUser
import os


class Command(BaseCommand):
    help = "Create superuser"

    def handle(self, *args, **kwargs):
        admin_username = os.environ.get("ADMIN_USERNAME")
        admin_email = os.environ.get("ADMIN_EMAIL")
        admin_password = os.environ.get("ADMIN_PASSWORD")

        if not CustomUser.objects.filter(username=admin_username).exists():
            admin = CustomUser.objects.create_superuser(username=admin_username, email=admin_email,
                                                        password=admin_password)
            admin.save()
            self.stdout.write(self.style.SUCCESS(f"User with username '{admin_username}' created"))
        else:
            self.stdout.write(self.style.ERROR(f"User with username '{admin_username}' already exists"))
