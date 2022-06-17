# Laboratorio 3.6.1.9
#Luis Daniel Sánchez Cabrera

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

listaOrdenada = []

for numero in my_list:
    if numero in listaOrdenada:
        continue
    else:
        listaOrdenada.append(numero)
print("La lista con elementos únicos:")
print(listaOrdenada)