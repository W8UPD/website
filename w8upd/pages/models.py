from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    body = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

