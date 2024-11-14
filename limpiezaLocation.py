import json
import pycountry

# Cargar el archivo JSON
with open('C:\\Users\\ASUS\\Desktop\\Hackaton\\locations.json', "r") as file:
    endangered_species_data = json.load(file)

# Función para obtener nombres de países de pycountry
def get_country_name(country_part):
    for country in pycountry.countries:
        if country.name in country_part:
            return country.name
    return None

# Extraer y almacenar países únicos
countries = set()
for item in endangered_species_data:
    location = item.get("Location(s)", "")
    for part in location.split(","):
        country = get_country_name(part.strip())
        if country:
            countries.add(country)

# Convertir el conjunto a una lista y guardar en JSON
countries_list = list(countries)
with open('C:\\Users\\ASUS\\Desktop\\Hackaton\\unique_countries.json', "w") as output_file:
    json.dump(countries_list, output_file, indent=4, ensure_ascii=False)

print("Países encontrados guardados en unique_countries.json.")
