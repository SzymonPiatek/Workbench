from django.core.management.base import BaseCommand
from django.db.models import Max
from localizations.models import Room
from items.models import Item, ItemType
import random


class Command(BaseCommand):
    help = "Create new items"

    def handle(self, *args, **kwargs):
        self.create_items()

    def create_items(self):
        rooms = Room.objects.all()

        items = [
            {"name": "Biurko", "item_type": "Biurko"},
            {"name": "Monitor", "item_type": "Monitor"},
            {"name": "Lampka", "item_type": "Lampka"},
            {"name": "Laptop", "item_type": "Laptop"},
            {"name": "Fotel", "item_type": "Fotel"},
        ]

        for item in items:
            result = ItemType.objects.filter(name=item["name"])
            if not result:
                ItemType.objects.create(name=item["name"])

        max_code = Item.objects.aggregate(max_code=Max('code'))['max_code']

        if max_code:
            max_code = int(max_code)
        else:
            max_code = 0

        def get_item_type(item_type):
            return ItemType.objects.filter(name=item_type).first()

        for room in rooms:
            for i in range(random.randint(1, 3)):
                for item in items:
                    new_item = Item.objects.create(
                        name=item["name"],
                        item_type=get_item_type(item["item_type"]),
                        code=max_code + 1,
                        room=room
                    )

        self.stdout.write(self.style.SUCCESS('Items created successfully.'))
        return True
