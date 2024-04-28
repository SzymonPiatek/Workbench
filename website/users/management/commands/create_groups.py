from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Create groups"

    def handle(self, *args, **kwargs):
        GROUPS = [
            "admin", "building_admin", "supervisor", "helpdesk", "worker"
        ]

        for group_name in GROUPS:
            Group.objects.get_or_create(name=group_name)
        self.stdout.write(self.style.SUCCESS("Groups created"))
