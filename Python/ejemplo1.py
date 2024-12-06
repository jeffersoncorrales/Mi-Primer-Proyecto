# Paso 1: Creación de un diccionario
libros = {
    "1984": {"autor": "George Orwell", "año": 1949, "género": "Distopía", "calificación": 4.8},
    "To Kill a Mockingbird": {"autor": "Harper Lee", "año": 1960, "género": "Ficción", "calificación": 4.9},
    "El Gran Gatsby": {"autor": "F. Scott Fitzgerald", "año": 1925, "género": "Ficción", "calificación": 4.3},
}

# Paso 2: Acceder a los valores de un diccionario
libro = "1984"
print(f"Detalles del libro '{libro}':")
print(f"Autor: {libros[libro]['autor']}")
print(f"Año de publicación: {libros[libro]['año']}")
print(f"Género: {libros[libro]['género']}")
print(f"Calificación: {libros[libro]['calificación']}")

# Paso 3: Modificar un valor dentro de un diccionario
libros["1984"]["calificación"] = 5.0
print(f"Nueva calificación de '1984': {libros['1984']['calificación']}")