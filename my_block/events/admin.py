from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'event_image', 'event_text')
    list_display_links = ('id', 'event_image')
    search_fields = ('data',)


class EventsBlonckAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'category', 'name', 'image', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('data', 'name', )
    list_editable = ('category', 'is_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', ' title')
    list_display_links = ('id', ' title')
    search_fields = ('title',)


admin.site.register(Event, EventAdmin)
admin.site.register(EventsBlonck, EventsBlonckAdmin)
admin.site.register(Category)
# Register your models here.
