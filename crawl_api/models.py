from django.db import models
from django.conf import settings


class Crawler(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key_words = models.JSONField()
    url = models.URLField()
    domain_title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.domain_title} - {self.owner}"


class Scrape(models.Model):
    created_by = models.ForeignKey(Crawler, on_delete=models.CASCADE)
    # TODO: make url mandatory
    url = models.URLField(null=True, blank=True)
    date = models.DateField(auto_now=True)
