from django.db import models
from users.models import CustomUser
from items.models import Item, ItemType


class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reservation_type = models.CharField(max_length=100, unique=True, blank=False, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_continuous = models.BooleanField(default=False)
    is_whole_day = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Rezerwacja"
        verbose_name_plural = "Rezerwacje"

    def __str__(self):
        return f"{self.item} - {self.user}"
