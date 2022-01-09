import os

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework_api_key.permissions import HasAPIKey
from decouple import config

from . import serializers, models

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR_FROM_ENV = config("SCRAPY_PROJECT")


###############################################################
# CRAWLER VIEWS                                               #
###############################################################
class CreateCrawlersApiView(generics.CreateAPIView):
    # TODO: figure out how this should work with the frontend
    # permission_classes = [IsAdminUser]
    serializer_class = serializers.CrawlerSerializer
    queryset = models.Crawler.objects.all()


class ListCrawlersApiView(generics.ListAPIView):
    permission_classes = [HasAPIKey | IsAdminUser]
    serializer_class = serializers.CrawlerSerializer
    queryset = models.Crawler.objects.all()


class ApiListCrawlersApiView(generics.ListAPIView):
    permission_classes = []
    serializer_class = serializers.CrawlerSerializer
    queryset = models.Crawler.objects.all()
    # TODO: filter queryset by user, authenticate user by token


class CrawlerApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.CrawlerSerializer
    queryset = models.Crawler.objects.all()


###############################################################
# SCRAPES VIEWS                                               #
###############################################################
class CreateScrapesApiView(generics.CreateAPIView):
    permission_classes = [HasAPIKey | IsAdminUser]
    serializer_class = serializers.ScrapeSerializer
    queryset = models.Scrape.objects.all()


class ListScrapesApiView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.ScrapeSerializer
    queryset = models.Scrape.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset
        # TODO: test filtering by token
        queryset = models.Scrape.objects.filter(created_by__owner__pk=self.request.user.pk)
        return queryset


class ScrapeApiView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.ScrapeSerializer
    queryset = models.Scrape.objects.all()
