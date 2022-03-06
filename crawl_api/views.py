import os

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from decouple import config

from . import serializers, models


###############################################################
# CRAWLER VIEWS                                               #
###############################################################
class CreateCrawlersApiView(generics.CreateAPIView):
    serializer_class = serializers.CrawlerSerializer
    queryset = models.Crawler.objects.all()


class ListCrawlersApiView(generics.ListAPIView):
    swagger_schema = None
    serializer_class = serializers.CrawlerSerializer
    queryset = models.Crawler.objects.all()


class ApiListCrawlersApiView(generics.ListAPIView):
    serializer_class = serializers.CrawlerSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.Crawler.objects.all()
        return models.Crawler.objects.all(owner=self.request.user)


class CrawlerApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CrawlerSerializer
    queryset = models.Crawler.objects.all()


###############################################################
# SCRAPES VIEWS                                               #
###############################################################
class CreateScrapesApiView(generics.CreateAPIView):
    swagger_schema = None
    serializer_class = serializers.ScrapeSerializer
    queryset = models.Scrape.objects.all()


class ListScrapesApiView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.ScrapeSerializer
    queryset = models.Scrape.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        # TODO: test filtering by user
        queryset = models.Scrape.objects.filter(created_by__owner=self.request.user)
        return queryset


class ScrapeApiView(generics.RetrieveDestroyAPIView):
    swagger_schema = None
    permission_classes = [IsAdminUser]
    serializer_class = serializers.ScrapeSerializer
    queryset = models.Scrape.objects.all()


###############################################################
# USER VIEW                                                   #
###############################################################
class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()
