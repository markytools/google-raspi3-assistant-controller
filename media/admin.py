from django.contrib import admin

# Register your models here.
from .models import Audio, Playlist

admin.site.register(Audio)
admin.site.register(Playlist)
