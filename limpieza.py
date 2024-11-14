import json
import pycountry

# Cargar el archivo JSON
with open(r'C:\Users\ASUS\Desktop\Hackaton\locations.json', 'r') as file:
    endangered_species_data = json.load(file)

# Función para obtener nombres de países de pycountry
def get_country_name(location_part):
    for country in pycountry.countries:
        if country.name in location_part:
            return country.name
    return None

# Añadir un nuevo campo 'Countries' con los nombres de los países extraídos
for item in endangered_species_data:
    location = item.get("Location(s)", "")
    countries = set()
    for part in location.split(","):
        country = get_country_name(part.strip())
        if country:
            countries.add(country)
    # Agregar los países encontrados al diccionario del item
    item["Countries"] = list(countries)

# Guardar el archivo actualizado con los países extraídos
with open(r'C:\Users\ASUS\Desktop\Hackaton\updated_locations.json', 'w') as file:
    json.dump(endangered_species_data, file, indent=4)
