from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    pass
