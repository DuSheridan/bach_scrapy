import os

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_api_key.permissions import HasAPIKey
from decouple import config

from . import serializers, models

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR_FROM_ENV = config("SCRAPY_PROJECT")


class CrawlersApiView(generics.ListCreateAPIView):
    serializer_class = serializers.CrawlerSerializer
    queryset = models.Crawler.objects.all()


class CrawlerApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CrawlerSerializer
    queryset = models.Crawler.objects.all()


class ScrapesApiView(generics.ListCreateAPIView):
    permission_classes = [HasAPIKey]
    serializer_class = serializers.ScrapeSerializer
    queryset = models.Scrape.objects.all()


class ScrapeApiView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.ScrapeSerializer
    queryset = models.Scrape.objects.all()
