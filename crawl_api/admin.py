from django.contrib import admin
from . import models
# Register your models here.


###############################################
# INLINE CLASSES                              #
###############################################
class ScrapeInline(admin.TabularInline):
    model = models.Scrape
    readonly_fields = ("created_by", "created_on")
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


@admin.register(models.ScrapeOverview)
class ScrapeOverviewAdmin(admin.ModelAdmin):
    # For read-only view
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
