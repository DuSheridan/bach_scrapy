from django.db import models
from django.conf import settings


# Create your models here.
class Test(models.Model):
    text = models.TextField()


class Crawler(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key_words = models.JSONField()


class Scrape(models.Model):
    url = models.URLField()
    created_by = models.ForeignKey(Crawler, on_delete=models.CASCADE)
