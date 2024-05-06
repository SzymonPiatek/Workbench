from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Create test database"

    def handle(self, *args, **kwargs):
        call_command("create_users", 100)
        call_command("create_groups")
        call_command("add_worker_group")
        call_command("create_superuser")
        call_command("add_superuser_to_groups")
        call_command("create_fake_addresses", 20)
        call_command("create_fake_rooms")
        call_command("create_fake_items")
