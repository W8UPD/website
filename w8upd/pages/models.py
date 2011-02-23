from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    body = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return "[%s] %s" % (self.category.name, self.title)

