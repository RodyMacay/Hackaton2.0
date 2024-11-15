from django.shortcuts import render
from django.views import View
import pandas as pd

from config.utils import filter_species_data, load_species_data, validate_filters

class SpeciesFilterView(View):
    def get(self, request, *args, **kwargs):
        # Ruta del archivo CSV
        file_path = 'C:/Hackaton2.0/db/final_ultimo3.1 (1).csv'

        try:
            # Cargar los datos del CSV usando pandas
            data = load_species_data(file_path)

            # Obtener los filtros de la solicitud
            filters = {
                'species_type': request.GET.get('species_type', None),
                'location': request.GET.get('location', None),
                'conservation_status': request.GET.get('conservation_status', None),
                'min_population': request.GET.get('min_population', 0),
                'max_population': request.GET.get('max_population', 1000),
            }

            # Validar los filtros
            filters = validate_filters(filters)

            # Convertir las poblaciones a enteros y aplicar los filtros de población
            min_population = int(filters['min_population'])
            max_population = int(filters['max_population'])

            # Filtrar los datos según los criterios de población
            data['Estimated Population'] = data['Estimated Population'].apply(self.convert_population_to_int)
            filtered_data = data[(data['Estimated Population'] >= min_population) & (data['Estimated Population'] <= max_population)]

            # Filtrar los datos con base en los filtros adicionales (tipo, ubicación, estado de conservación)
            filtered_data = filter_species_data(filtered_data, filters)

            # Extrae los nombres de conservación y pásalos como un contexto
            conservation_names = data['Conservation Name'].unique()


            context = {
                'filtered_data': filtered_data.to_dict(orient='records'),
                'filters': filters,
                'species_types': data['Type'].unique(),
                'locations': data['País'].unique(),
                'conservation_names': conservation_names,  # Solo los nombres de conservación
            }




            # Renderizar la plantilla y pasar los datos filtrados
            return render(request, 'app/tipo_especie/tipo_especie.html', context)

        except ValueError as e:
            return render(request, 'app/tipo_especie/tipo_especie.html', {"error": str(e)})

    def convert_population_to_int(self, population_str):
        """
        Convierte el valor de población de texto (como '10 sub-populations') a un número entero.
        """
        try:
            # Extraemos solo el número de la población, eliminando cualquier texto adicional
            population = int(''.join(filter(str.isdigit, population_str)))
            return population
        except ValueError:
            return 0  # Si no se puede convertir, devolvemos 0
