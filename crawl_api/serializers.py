from rest_framework import serializers

from . import models


class CrawlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Crawler
        fields = '__all__'


class ScrapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scrape
        fields = '__all__'


class ScrapeOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ScrapeOverview
        exclude = ('user_id', 'owner_id', 'crawler_id', 'created_by_id')
