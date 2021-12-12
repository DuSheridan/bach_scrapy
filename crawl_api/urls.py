from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
    openapi.Info(title='Crawl API', default_version='v1',
                 description="Documentation for the Crawl API")
    )
urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger__schema_view"),
    path('auth/', obtain_auth_token, name='token_auth'),
    path('crawlers/', views.CreateCrawlersApiView.as_view(), name="create_crawlers"),
    path('crawlers/<int:pk>/', views.CrawlerApiView.as_view(), name="crawler"),
    path('admin/crawlers/', views.ListCrawlersApiView.as_view(), name="crawlers"),
    path('admin/scrapes/', views.ListScrapesApiView.as_view(), name="scrapes"),
    path('scrapes/', views.CreateScrapesApiView.as_view(), name="create_scrapes"),
    path('scrapes/<int:pk>/', views.ScrapeApiView.as_view(), name="scrape")
]
