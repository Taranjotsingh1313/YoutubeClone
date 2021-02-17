from django.urls import path
from . import views
urlpatterns = [
    path('',views.youtubehomepageclone,name='youtubehomepageclone'),
]