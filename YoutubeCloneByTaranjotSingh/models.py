from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class YoutubeVideoUpload(models.Model):
    video_title = models.CharField(max_length=255)
    video_desc = models.TextField()
    video = models.FileField(upload_to='videos')
    video_user = models.ForeignKey(User,on_delete=models.CASCADE)