from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('start-crawl', views.start_crawling),
    path('crawlers/', views.CrawlersApiView.as_view(), name="crawlers"),
    path('crawlers/<int:pk>/', views.CrawlerApiView.as_view(), name="crawler"),
    path('scrapes', views.ScrapesApiView.as_view(), name="scrapes"),
    path('scrapes/<int:pk>/', views.ScrapeApiView.as_view(), name="scrape")
]
