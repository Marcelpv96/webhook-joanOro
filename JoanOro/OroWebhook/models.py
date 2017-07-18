from django.db import models
from django.utils import timezone

from django_hstore import hstore
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
    date_received = models.DateTimeField(default=timezone.now)
    body = hstore.SerializedDictionaryField()
    request_meta = hstore.SerializedDictionaryField()
    status = models.CharField(max_length=250, choices=STATUSES, default=UNPROCESSED)

    objects = hstore.HStoreManager()

    def __unicode__(self):
        return u'{0}'.format(self.date_event_generated)


