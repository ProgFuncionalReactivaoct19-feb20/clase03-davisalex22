"""
Clase 3: Practica 1

Autor: @davisalex22

"""
# Dado un conjunto de palabras ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]
#  filtrar todas aquellas que sean palindromas


palabras = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]    
resultado = filter(lambda x: "".join(reversed(x)) == x, palabras)

print(resultado)

print(list(resultado)) 








