import csv
import json

# Ruta del archivo CSV
file_path = r'C:\Users\ASUS\Desktop\Hackaton\Species.csv'
# Ruta del archivo JSON de salida
output_json_path = r'C:\Users\ASUS\Desktop\Hackaton\locations.json'

# Lista para almacenar las ubicaciones
locations = []

# Leer el archivo CSV y extraer solo la columna "Location(s)"
with open(file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Agregar solo la columna "Location(s)" a la lista
        locations.append({"Location(s)": row["Location(s)"]})

# Guardar la lista en un archivo JSON
with open(output_json_path, mode='w', encoding='utf-8') as json_file:
    json.dump(locations, json_file, indent=4, ensure_ascii=False)

print(f"Datos guardados en {output_json_path}")
