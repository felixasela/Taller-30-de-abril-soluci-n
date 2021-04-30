# Opción 1
# Parte entera y parte decimal de un número
decimal = float(input("Ingrese un número decimal = "))
#Proceso separar parte entera
entero = int(decimal)
print("La parte entera es = " + str(entero) + "\n")
#Proceso para separar la parte decimal de la entera
decimal2 = float(entero - decimal)
print("La parte decimal es = " + str(decimal2) + "\n")

# Opción 2
import math
numero = float(input("Digite un numero: "))
print("El número es: ", numero)
decimal, entera = math.modf(numero)
print("Su parte entera es = " + str(entera))
print("Su parte decimal es = " + str(decimal))