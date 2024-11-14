# urls.py
from django.urls import path

from .views import geografico

urlpatterns = [
    path('biodiversity-map/', geografico.BiodiversityMapView.as_view(), name='biodiversity_map'),
]
