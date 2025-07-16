from django.urls import path

from . import views

app_name = "api_music"

urlpatterns = [
    path("", views.NowPlayingView.as_view(), name="index"),
]
