from django.urls import path
from .views import HomePageView, MapView, AboutMeView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("map/", MapView.as_view(), name="map"),
    path("aboutme/", AboutMeView.as_view(), name="aboutme"),
]
