from django.db import models
from Person.models import Person


class Event(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to='events/',
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=50
    )

    state = models.CharField(
        max_length=50
    )

    nbre_participant = models.PositiveIntegerField(
        default=0
    )

    evt_date = models.DateTimeField()

    creation_date = models.DateTimeField(
        auto_now_add=True
    )

    update_date = models.DateTimeField(
        auto_now=True
    )

    organizer = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='organized_events'
    )

    def __str__(self):
        return self.title


class Participation(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='participations'
    )

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='participations'
    )

    participation_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['event', 'person'],
                name='unique_event_person'
            )
        ]

    def __str__(self):
        return f"{self.person} - {self.event}"