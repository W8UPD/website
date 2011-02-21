from django.db import models
from django.contrib.auth.models import User

MODE_CHOICES = (
    ('USB', 'Upper Sideband (USB)'),
    ('LSB', 'Lower Sideband (LSB)'),
    ('FM', 'Frequency Modulaion (FM)'),
    ('AM', 'Amplitude Modulation (AM)'),
    ('CW', 'Continuous Wave (CW)'),
    ('DIG', 'Digital Mode'),
    ('OTH', 'Other'),
)

class Contact(models.Model):
    callsign = models.CharField(max_length=8)
    received = models.CharField(max_length=10)
    sent = models.CharField(max_length=10)
    time = models.DateTimeField()
    operator = models.ForeignKey(User)
    mode = models.CharField(max_length=3, choices=MODE_CHOICES)
    frequency = models.DecimalField(max_digits=10, decimal_places=2, help_text="Frequency of the contact in KHz")

    def __unicode__(self):
        return "Contact with %s at %s" % (self.callsign, self.time)
 
