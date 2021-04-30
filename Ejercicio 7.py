# valor original, el valor del IVA y el valor de la venta con IVA incluido
Valor = int(input("Ingrese el valor del producto: $ "))
IVA = 0.19
Valorconiva = (Valor * IVA) + Valor
Valordeliva = 0.19 * Valor / 100
print("El precio del producto sin IVA es: ", Valor)
print("El precio del producto con IVA es: ", Valorconiva)
print("El precio del IVA es: ", Valordeliva)