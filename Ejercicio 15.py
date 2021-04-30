# energía (en Julios) de un objeto
# Variables y constantes
masa = float(input("Ingres el valor de la masa del objeto en kg = "))
velocidadLuz = 299792.458
#Procesos
energia = masa * (pow(velocidadLuz, 2))
print("La energía del objeto es = " + str(energia) + " Julios(J)")
