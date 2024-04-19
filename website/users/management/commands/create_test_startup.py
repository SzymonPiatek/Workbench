from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.hashers import make_password
from users.models import CustomUser


class Command(BaseCommand):
    help = "Create test startup"

    def handle(self, *args, **kwargs):
        self.create_superuser()
        self.create_test_users()

    def create_superuser(self):
        if CustomUser.objects.filter(username="admin").exists():
            self.stdout.write(self.style.ERROR("User with username 'admin' already exists"))
        else:
            call_command(command_name="createsuperuser",
                         username="admin",
                         email="admin@admin.pl",
                         interactive=False)

    def create_test_users(self):
        call_command("create_fake_users", 100)
