from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Test create users"

    def handle(self, *args, **kwargs):
        call_command("create_fake_users", 1)
        call_command("create_fake_users", 2)
        call_command("create_fake_users", 4)
        call_command("create_fake_users", 8)
        call_command("create_fake_users", 16)
        call_command("create_fake_users", 32)
        call_command("create_fake_users", 64)
        call_command("create_fake_users", 128)
        call_command("create_fake_users", 256)
        call_command("create_fake_users", 512)
        call_command("create_fake_users", 1024)
