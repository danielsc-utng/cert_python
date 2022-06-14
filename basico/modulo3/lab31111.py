# Laboratorio 3.1.1.11
#Luis Daniel Sánchez Cabrera

income=float(input("Introduce el ingreso anual:"))


if income < 85_528:
    ing=income * 0.18 
    tax=ing - 556.02
else:
    tax=14839.02+(income-85528)*0.32
tax=round(tax, 0)
print("El impuesto es:", tax, "pesos")
