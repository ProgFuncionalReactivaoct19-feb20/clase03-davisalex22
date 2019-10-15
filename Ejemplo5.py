def es_vocal(x):
	vocales = ["l", "p", "a", "i","e"]
    if x[0] in vocales:
		return True
	else:
		return False

placas = ["lba-001", "gma-002", "azx-003",
    "ess-004", "oro-100", "mab-001", "iaj-002"] 

resultado = filter(es_vocal, placas)

print(list(resultado))
