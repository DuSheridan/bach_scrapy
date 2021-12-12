from django.contrib import admin
from . import models
# Register your models here.


###############################################
# INLINE CLASSES                              #
###############################################
class ScrapeInline(admin.TabularInline):
    model = models.Scrape
    readonly_fields = ("created_by", "date")
    extra = 0


###############################################
# ADMIN CLASSES                               #
###############################################
@admin.register(models.Scrape)
class ScrapeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Crawler)
class CrawlerAdmin(admin.ModelAdmin):
    inlines = [ScrapeInline]
