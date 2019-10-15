"""
Clase 3: Practica 1

Autor: @davisalex22

"""
# Dado un conjunto de palabras ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]
#  filtrar todas aquellas que sean palindromas


# Declaracion de cadena

palabras = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]

# Uso de función lambda y filter

resultado = filter(lambda x: "".join(reversed(x)) == x, palabras)

# Presentacion de resultados por pantalla

print(list(resultado))
