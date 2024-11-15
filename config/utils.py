import pandas as pd

def load_species_data(file_path):
    """
    Carga el archivo CSV con los datos de especies.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise ValueError(f"Error al cargar el archivo CSV: {e}")

def validate_filters(filters):
    """
    Valida los filtros recibidos.
    """
    valid_species_types = ["Planta (Árbol)", "Insecto", "Mamífero", "Reptil", "Otro"]
    valid_conservation_status = ["En Peligro", "En Peligro Crítico", "Preocupación Menor", "Desconocido"]

    # Validación de tipo de especie
    if filters.get("species_type") and filters["species_type"] not in valid_species_types:
        raise ValueError(f"Tipo de especie inválido. Valores válidos: {valid_species_types}")

    # Validación de estado de conservación
    if filters.get("conservation_status") and filters["conservation_status"] not in valid_conservation_status:
        raise ValueError(f"Estado de conservación inválido. Valores válidos: {valid_conservation_status}")

    # Validación del rango de población
    try:
        min_population = int(filters.get("min_population", 0))
        max_population = int(filters.get("max_population", 1000))
    except ValueError:
        raise ValueError("Los valores de población deben ser enteros válidos.")

    # Verificar que min_population sea menor que max_population
    if min_population > max_population:
        raise ValueError("El valor de la población mínima no puede ser mayor que la población máxima.")

    return filters

def filter_species_data(data, filters):
    """
    Filtra los datos de especies según los filtros proporcionados.
    """
    # Filtrar por tipo de especie
    if filters.get("species_type"):
        data = data[data['Type'] == filters["species_type"]]

    # Filtrar por ubicación
    if filters.get("location"):
        data = data[data['Location(s)'].str.contains(filters["location"], case=False, na=False)]

    # Filtrar por estado de conservación
    if filters.get("conservation_status"):
        data = data[data['Conservation Status'] == filters["conservation_status"]]

    # Filtrar por rango de población
    if filters.get("min_population") and filters.get("max_population"):
        data = data[(data['Estimated Population'] >= filters["min_population"]) &
                    (data['Estimated Population'] <= filters["max_population"])]

    return data
