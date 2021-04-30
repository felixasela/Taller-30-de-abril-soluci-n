# Programa que dada una cantidad de segundos indique cuántos horas minutos y segundos representan.
#Definir variables y constantes
valor = int(input("Ingrese el valor que desea convertir = "))
segundosHora = 3600
segundosMinutos = 60
#Proceso
hora = int(valor / segundosHora)
minutos = int((valor - (hora*segundosHora)) / 60)
segundos = valor - ((hora * 3600) + (minutos*60))
print("La hora es = " + str(hora) + ":" + str(minutos) + ":" + str(segundos))