from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('player/', views.Player.as_view(), name='player'),
    path('api/', include('music.api.urls')),
]
