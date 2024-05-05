from django.db import models
from localizations.models import Room


class ItemType(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE, default=None, blank=False)
    code = models.CharField(max_length=100, blank=False, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Przedmiot"
        verbose_name_plural = "Przedmioty"

    def __str__(self):
        return f"{self.name} ({self.code})"
