from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.hashers import make_password
from users.models import CustomUser
import os


class Command(BaseCommand):
    help = "Create test startup"

    def handle(self, *args, **kwargs):
        self.create_superuser()
        self.create_test_users()
        self.create_test_addresses()

    def create_superuser(self):
        if CustomUser.objects.filter(username=os.environ.get("ADMIN_USERNAME")).exists():
            self.stdout.write(self.style.ERROR(f"User with username '{os.environ.get("ADMIN_USERNAME")}' already exists"))
        else:
            call_command(command_name="createsuperuser",
                         username=os.environ.get("ADMIN_USERNAME"),
                         email=os.environ.get("ADMIN_EMAIL"),
                         interactive=False)

            admin = CustomUser.objects.get(username=os.environ.get("ADMIN_USERNAME"))
            admin.set_password(os.environ.get("ADMIN_PASSWORD"))
            admin.save()

    def create_test_users(self):
        call_command("create_fake_users", 100)

    def create_test_addresses(self):
        call_command("create_fake_addresses", 100)
