#Definir variables
tiempo = float(input("Ingrese el valor del tiempo en hora = "))
aceleracion = float(input("Ingrese el valor de la aceleración en m/s2 = "))
velocidad = float(input("Ingrese el valor de la velocidad en m/s = "))
#Proceso
distancia = (velocidad * tiempo) + 1/2 *(aceleracion*pow(tiempo, 2))
#IMPRIMIR
print()
print("La distancia recorrida por el objeto es = " + str(distancia) + " m/s" )
print("¡El programa se ha terminado de ejecutar con éxito!")
