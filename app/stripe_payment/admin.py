from django.contrib import admin

from .models import Item


# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_filter = ("price",)
    search_fields = ("name", "description")
    ordering = ("name",)
