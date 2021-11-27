import os

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, generics
from rest_framework.response import Response
from decouple import config
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from . import serializers, models

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR_FROM_ENV = config("SCRAPY_PROJECT")


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def start_crawling(request):
    # process = CrawlerProcess(get_project_settings())
    # hello = 2

    return Response(status=200)


class CrawlersApiView(generics.ListCreateAPIView):
    serializer_class = serializers.CrawlerSerializer
    queryset = models.Crawler.objects.all()


class CrawlerApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CrawlerSerializer
    queryset = models.Crawler.objects.all()


class ScrapesApiView(generics.ListCreateAPIView):
    serializer_class = serializers.ScrapeSerializer
    queryset = models.Scrape.objects.all()


class ScrapeApiView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.ScrapeSerializer
    queryset = models.Scrape.objects.all()
