from django.shortcuts import render
from django.views import View
import pandas as pd

from config.utils import filter_species_data, load_species_data, validate_filters

class SpeciesFilterView(View):
    def get(self, request, *args, **kwargs):
        file_path = 'C:/Hackaton2.0/db/final_ultimo3.1 (1).csv'
        
        try:
            print("Cargando datos del archivo:", file_path)
            data = load_species_data(file_path)
            print("Datos cargados con éxito. Filas:", data.shape[0])

            filters = {
                'species_type': request.GET.get('species_type', None),
                'location': request.GET.get('location', None),
                'conservation_status': request.GET.get('conservation_status', None),
                'min_population': request.GET.get('min_population', 0),
                'max_population': request.GET.get('max_population', 1000),
            }
            print("Filtros iniciales:", filters)

            filters = validate_filters(filters)
            print("Filtros validados:", filters)

            # Explora los valores únicos antes de la conversión
            print("Valores únicos en Estimated Population:", data['Estimated Population'].unique())

            data['Estimated Population'] = data['Estimated Population'].apply(self.convert_population_to_int)
            print("Población convertida. Ejemplo:", data['Estimated Population'].head())

            min_population = int(filters['min_population'])
            max_population = int(filters['max_population'])
            filtered_data = data[(data['Estimated Population'] >= min_population) & (data['Estimated Population'] <= max_population)]
            print("Filtrado por población. Filas restantes:", filtered_data.shape[0])

            filtered_data = filter_species_data(filtered_data, filters)
            print("Filtrado por criterios adicionales. Filas restantes:", filtered_data.shape[0])

            conservation_names = data['Conservation Name'].unique()
            context = {
                'filtered_data': filtered_data.to_dict(orient='records'),
                'filters': filters,
                'species_types': data['Type'].unique(),
                'locations': data['País'].unique(),
                'conservation_names': conservation_names,
            }
            print("Contexto preparado:", context.keys())

            return render(request, 'app/tipo_especie/tipo_especie.html', context)
        
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            return render(request, 'app/tipo_especie/tipo_especie.html', {"error": str(e)})

    def convert_population_to_int(self, population_str):
        try:
            if population_str == "Unknown":
                return 0
            if "few hundred pairs" in str(population_str).lower():
                return 200
            population = int(''.join(filter(str.isdigit, str(population_str))))
            return population
        except ValueError:
            print(f"Error convirtiendo población: {population_str}")
            return 0
