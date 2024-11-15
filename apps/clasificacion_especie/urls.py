from django.urls import path

from apps.clasificacion_especie.views.clasificacion_especie import SpeciesFilterView

urlpatterns = [
    path('filter-species/', SpeciesFilterView.as_view(), name='filter_species'),
]
