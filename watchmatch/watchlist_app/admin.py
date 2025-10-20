from django.contrib import admin
# from .models import Movie
from .models import WatchList, StreamPlatform

# @admin.register(Movie)
# class MovieAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'description', 'active']

@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'storyline', 'active', 'created']
@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'about', 'website']