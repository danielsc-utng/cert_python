# Laboratorio 3.4.1.13
#Luis Daniel Sánchez Cabrera

# paso 1
Beatles=[]
print("Paso 1:", Beatles)
# paso 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# paso 3
for i in range(2):
    integrantes= input("Agrega el nombre del nuevo integrante: ")
    Beatles.append(integrantes)
print("Paso 3:", Beatles)

# paso 4
print("Paso 4:", Beatles)
del Beatles[3]
del Beatles[3]
# paso 5
Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)

# probando la longitud de la lista
print("Los Fav", len(Beatles))
