from rest_framework import serializers
from django.contrib.auth import get_user_model

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


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password')
