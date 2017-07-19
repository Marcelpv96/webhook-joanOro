from django.db import models
from django.utils import timezone

# Create your models here.


class WebhookTransaction(models.Model):
    UNPROCESSED = 1
    PROCESSED = 2
    ERROR = 3

    STATUSES = (
        (UNPROCESSED, 'Unprocessed'),
        (PROCESSED, 'Processed'),
        (ERROR, 'Error'),
    )

    date_generated = models.DateTimeField()


    def __unicode__(self):
        return u'{0}'.format(self.date_event_generated)


