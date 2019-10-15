
"""
Clase 3: Practica 3

Autor: @davisalex22

"""
# Dadas las siguiente ciudades, filtrar aquellas que tienen un número par como longitud en sus caracteres.
# Loja, Pichincha, Guayaquil, Zamora, Ibarra, Manabi, Machala,  Portoviejo, Macas

# Declaracion de cadena

ciudad = ["Loja", "Pichincha", "Guayaquil", "Zamora",
          "Ibarra", "Manabi", "Machala", "Portoviejo", "Macas"]

# Uso de función lambda y filter

result = filter(lambda x: len(x) % 2 == 0, ciudad)

# Presentacion de resultados por pantalla

print(list(result))
