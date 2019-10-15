"""
Clase 3: Practica 2

Autor: @davisalex22

"""
# Dada las siguientes placas, filtrar aquellas que pertenecen a las provincias de :
# Loja, Pichincha, Esmeraldas, Azuay, Imbabura
# Placas: lba-001, gma-002, azx-003, ess-004,  oro-100, mab-001, iaj-002


def ident_vocal(x):
    vocales = ["l", "p", "a", "i", "e"]
    if x[0] in vocales:
        return True
    else:
        return False


placas = ["lba-001", "gma-002", "azx-003",
          "ess-004", "oro-100", "mab-001", "iaj-002"]

resultado = filter(ident_vocal, placas)

# Presentacion de resultados por pantalla

print(list(resultado))
