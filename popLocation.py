import json

# Cargar el archivo JSON
with open('C:/Users/ASUS/Desktop/Hackaton/especies_limpias.json', 'r') as file:
    endangered_species_data = json.load(file)

# Eliminar la clave "location" de cada elemento
for item in endangered_species_data:
    item.pop("location", None)

# Guardar los cambios en un nuevo archivo JSON
with open('C:/Users/ASUS/Desktop/Hackaton/locations_no_location.json', 'w') as file:
    json.dump(endangered_species_data, file, indent=4)

print("Clave 'location' eliminada de cada elemento y archivo guardado como 'locations_no_location.json'")
