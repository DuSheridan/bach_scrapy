from django.contrib import admin
from . import models
# Register your models here.


###############################################
# INLINE CLASSES                              #
###############################################
class ScrapeInline(admin.TabularInline):
    model = models.Scrape


###############################################
# ADMIN CLASSES                               #
###############################################
@admin.register(models.Scrape)
class ScrapeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Crawler)
class CrawlerAdmin(admin.ModelAdmin):
    inlines = [ScrapeInline]
