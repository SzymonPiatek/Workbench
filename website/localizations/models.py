from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    room_type = models.CharField(max_length=100, blank=False, null=False)
    floor = models.IntegerField(blank=False, null=False)

    class Meta:
        verbose_name = "Pomieszczenie"
        verbose_name_plural = "Pomieszczenia"


class Address(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    apartment_number = models.CharField(max_length=10, blank=True, null=True)
    zip_code = models.CharField(max_length=10)
    zip_code_city = models.CharField(max_length=100)
    voivodeship = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Adres"
        verbose_name_plural = "Adresy"

    def __str__(self):
        return self.name
