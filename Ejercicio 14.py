# Velocidad final de un objeto
velocidadInicial = float(input("Ingrese el valor de la velocidad inicial = "))
aceleracion = float(input("Ingrese el valor de la aceleración = "))
tiempo = float(input("Ingrese el valor del tiempo en segundos = "))
#PROCESOS
velocidadFinal = velocidadInicial + (aceleracion * tiempo)
print("La velocidad final del objeto es = ", velocidadFinal)