# Laboratorio 3.2.1.11
#Luis Daniel Sánchez Cabrera

c0 = int(input("Ingresa el numero: "))

if c0 < 1:
    print("Es necesario un número que no sea negativo o 0")
    exit
else:
    pasos = 0
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
        else:
            c0= 3 * c0 + 1
        print(int(c0))
        pasos = pasos + 1
print("Pasos: ", pasos)