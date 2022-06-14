# Laboratorio 3.1.1.12
#Luis Daniel Sánchez Cabrera

year=int(input("Introduce un año: "))


if(year <= 1580):
    print("NO esta dentro del periodo del calendario Gregoriano")
elif not (year % 4 == 0):
    print("Año común")
elif not(year % 100 == 0):
    print("Año bisiesto")
elif not(year % 400 == 0):
    print("Año común")
else:
    print("Año bisiesto")