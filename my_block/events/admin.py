from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'event_image', 'event_text')
    list_display_links = ('id', 'event_image')
    search_fields = ('event_image')


class EventsBlonckAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'name', 'image', 'test')
    list_display_links = ('id', 'name')
    search_fields = ('name')


admin.site.register(Event)
admin.site.register(EventsBlonck)
# Register your models here.
