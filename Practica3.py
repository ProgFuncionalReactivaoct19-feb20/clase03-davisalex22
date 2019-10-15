
"""
Clase 3: Practica 3

Autor: @davisalex22

"""
# Dadas las siguiente ciudades, filtrar aquellas que tienen un número par como longitud en sus caracteres.
# Loja, Pichincha, Guayaquil, Zamora, Ibarra, Manabi, Machala,  Portoviejo, Macas

ciudad = ["Loja","Pichincha","Guayaquil","Zamora","Ibarra","Manabi","Machala","Portoviejo","Macas"]

result = filter(lambda x: len(x)%2 == 0,ciudad)

print(list(result))