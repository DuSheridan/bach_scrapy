from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('start-crawl', views.start_crawling),
    path('crawlers/', views.CrawlersApiView, name="crawlers"),
    path('crawlers/<int:pk>', views.CrawlerApiView, name="crawler"),
    path('scrapes/', views.ScrapesApiView, name="scrapes"),
    path('scrapes/<int:pk>', views.ScrapeApiView, name="scrape")
]
