import csv
import json

# Abre el archivo CSV
with open(r'C:\Users\ASUS\Desktop\Hackaton\Species.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = [row for row in csv_reader]

# Guarda los datos en formato JSON
with open('especies_en_peligro.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
