#imprima el área y el perímetro de un círculo
pi = 3.1416
radio = int(input("Ingrese el radio del círculo: "))

area = (pi)*(radio**2)
perimetro = (2*pi) * radio

print("El área del círculo es: ", area)
print("El perímetro del círculo es: ", perimetro)