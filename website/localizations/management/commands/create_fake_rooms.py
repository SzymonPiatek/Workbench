from django.core.management.base import BaseCommand
from localizations.models import Address, Room
from users.models import CustomUser
import random
import time


class Command(BaseCommand):
    help = "Create new rooms"

    def handle(self, *args, **kwargs):
        self.start_time = time.time()
        self.create_rooms()

    def create_rooms(self):
        addresses = Address.objects.all()

        rooms = [
            {"name": "Recepcja", "room_type": "Recepcja", "floor": 0},
            {"name": "Pokój nr 1", "room_type": "Biuro", "floor": 0},
            {"name": "Pokój nr 2", "room_type": "Biuro", "floor": 1},
            {"name": "Pokój nr 3", "room_type": "Biuro", "floor": 1},
            {"name": "Pokój nr 4", "room_type": "Biuro", "floor": 1},
        ]

        for address in addresses:
            for room in rooms:
                new_room = Room.objects.create(
                    name=room["name"],
                    room_type=room["room_type"],
                    floor=room["floor"],
                    address=address
                )

        elapsed_time = time.time() - self.start_time
        self.stdout.write(self.style.SUCCESS(f'Rooms created in {elapsed_time:.2f} sec'))
