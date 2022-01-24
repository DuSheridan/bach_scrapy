import os

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from django.contrib.auth import get_user_model
from decouple import config

from . import serializers, models

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR_FROM_ENV = config("SCRAPY_PROJECT")


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
    queryset = models.Crawler.objects.all()
    # TODO: filter queryset by user


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
        if self.request.user.is_staff:
            return self.queryset
        # TODO: test filtering by token
        queryset = models.Scrape.objects.filter(created_by__owner__pk=self.request.user.pk)
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
    # permission_classes = [DjangoModelPermissions]
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()
