from django.contrib import admin
from .models import YoutubeVideoUpload
# Register your models here.
@admin.register(YoutubeVideoUpload)
class YoutubeVideoAdmin(admin.ModelAdmin):
    list_display = ['id','video_title']