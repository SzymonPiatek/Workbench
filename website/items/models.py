from django.db import models
from localizations.models import Room


class Item(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    code = models.CharField(max_length=100, blank=False, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Przedmiot"
        verbose_name_plural = "Przedmioty"

    def __str__(self):
        return f"{self.name} ({self.code})"


class ItemType(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    item = models.ManyToManyField(Item)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.name

    def item_count(self):
        return self.item.count()
