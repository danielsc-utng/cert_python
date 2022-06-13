# Laboratorio 2.6.1.11
#Luis Daniel Sánchez Cabrera

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.
minutos=mins+dura
minutosTotales=minutos%60
minutosReales=minutos//60
horasTotales=hour+minutosReales
horasReales=horasTotales%24
print("El evento termina a las: "+str(horasReales)+":"+str(minutosTotales))
