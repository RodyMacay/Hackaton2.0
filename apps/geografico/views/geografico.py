# views.py
from django.views.generic import TemplateView
import json
from django.conf import settings
import os

class BiodiversityMapView(TemplateView):
    template_name = "geografico/biodiversity_map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Cambia la ruta para buscar en 'public/static/data/especies_en_peligro.json'
        json_path = os.path.join(settings.STATICFILES_DIRS[0], "data/especies_en_peligro.json")
        with open(json_path, 'r', encoding='utf-8') as file:
            species_data = json.load(file)
        
        context['species_data'] = species_data
        return context
