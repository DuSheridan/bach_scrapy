from rest_framework import serializers

from . import models


class CrawlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Crawler


class ScrapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scrape
