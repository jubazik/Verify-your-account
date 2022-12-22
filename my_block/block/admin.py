from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','date', 'title', 'text', 'image')
    list_display_links = ('id', 'title')
    ordering = ('date',)


class RecordsAmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'name', 'sum', 'coment')
    list_display_links = ('id', 'name')
    ordering = ('name',)

class СounterpartiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'name', 'surname', 'firma', 'phone', 'image')
    list_display_links = ('id', 'name', 'surname')
    ordering = ('name', 'surname', 'image')



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Records, RecordsAmin)
admin.site.register(Сounterparties, СounterpartiesAdmin)



# Register your models here.
