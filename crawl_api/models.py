from django.db import models
from django.conf import settings
from crawl_api.notification_lib import create_and_send_mail


class Crawler(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key_words = models.JSONField()
    url = models.URLField()
    domain_title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.domain_title} - {self.owner}"


class Scrape(models.Model):
    created_by = models.ForeignKey(Crawler, on_delete=models.CASCADE)
    url = models.URLField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_by} - {self.created_on}"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        create_and_send_mail(self.created_by.owner, self.url, self.created_by.domain_title)
        return super().save(force_insert, force_update, using, update_fields)


class ScrapeOverview(models.Model):
    domain_title = models.CharField(max_length=100)
    url = models.URLField()
    email = models.CharField(max_length=254, null=True, blank=True)
    scrape_date = models.DateTimeField()
    user_id = models.IntegerField()
    owner_id = models.IntegerField()
    crawler_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()

    def __str__(self):
        return f"{self.crawler_id} - {self.scrape_date}"

    class Meta:
        # For views
        db_table = "scrape_overview"
        managed = False
