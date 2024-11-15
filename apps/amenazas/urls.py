# urls.py
from django.urls import path

from .views import amenazas

urlpatterns = [
    path('amenazas/', amenazas.AmenazasView.as_view(), name='biodiversity_map'),
]
