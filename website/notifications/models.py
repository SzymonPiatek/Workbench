from django.db import models
from users.models import CustomUser


class Notification(models.Model):
    TYPE_LIST = (
        ("single_use", "Jednorazowe"),
        ("cyclical", "Cykliczne"),
        ("reminder", "Przypomnienie"),
    )

    title = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    notification_type = models.CharField(max_length=50, choices=TYPE_LIST, default=TYPE_LIST[0])

    date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    time_before = models.TimeField(blank=True, null=True)
    recipients = models.ManyToManyField(CustomUser)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-is_active', '-created_at', '-notification_type']

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

    def is_active_return(self):
        return "Tak" if self.is_active else "Nie"
