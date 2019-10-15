"""
Clase 3: Funciones 

Autor: @davisalex22

"""



# Funcional - Aplicando función filter

datos = [1,2,10,11,12,13]

resultado = filter(lambda x: x % 2 == 0, datos)

print(resultado)

print(list(resultado)) 