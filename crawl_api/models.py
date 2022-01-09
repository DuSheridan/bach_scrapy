from django.db import models
from django.conf import settings


class Crawler(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key_words = models.JSONField()
    url = models.URLField()
    domain_title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.domain_title} - {self.owner}"


class Scrape(models.Model):
    created_by = models.ForeignKey(Crawler, on_delete=models.CASCADE)
    # TODO: make url mandatory
    url = models.URLField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)


class ScrapeOverview(models.Model):
    domain_title = models.CharField(max_length=100)
    # TODO: make url mandatory
    url = models.URLField(null=True, blank=True)
    email = models.CharField(max_length=254, null=True, blank=True)
    scrape_date = models.DateTimeField()
    user_id = models.IntegerField()
    owner_id = models.IntegerField()
    crawler_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()

    class Meta:
        # For views
        db_table = "scrape_overview"
        managed = False
