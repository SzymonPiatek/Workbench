from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
import time


class Command(BaseCommand):
    help = "Create groups"

    def handle(self, *args, **kwargs):
        start_time = time.time()

        GROUPS = [
            "admin", "building_admin", "supervisor", "helpdesk", "worker"
        ]

        for group_name in GROUPS:
            Group.objects.get_or_create(name=group_name)

        elapsed_time = time.time() - start_time
        self.stdout.write(self.style.SUCCESS(f"Groups created in {elapsed_time:.2f} sec"))
