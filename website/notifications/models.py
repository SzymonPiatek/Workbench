from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Notification(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(blank=False, null=False)
    frequency = models.IntegerField()
    recipients = models.ManyToManyField(User)

    class Meta:
        ordering = ['-created_at', '-start_date', '-frequency']

        verbose_name = 'Powiadomienie'
        verbose_name_plural = 'Powiadomienia'

    def __str__(self):
        return self.title

    def count_recipients(self):
        return self.recipients.count()

    def formatted_created_at(self):
        return self.created_at.strftime("%d.%m.%Y %H:%M")

    def match_weekday(self, weekday):
        match weekday:
            case 'Monday':
                return 'Poniedziałek'
            case 'Tuesday':
                return 'Wtorek'
            case 'Wednesday':
                return 'Środa'
            case 'Thursday':
                return 'Czwartek'
            case 'Friday':
                return 'Piątek'
            case 'Saturday':
                return 'Sobota'
            case 'Sunday':
                return 'Niedziela'

    def formatted_start_date(self):
        date = self.start_date.strftime("%d.%m.%Y %H:%M")
        weekday = self.start_date.strftime("%A")
        weekday = self.match_weekday(weekday)
        full_date = f"{date} {weekday}"

        return full_date
