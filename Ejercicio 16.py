# Fistancia entre los puntos x1,y1 y x2,y2
#Definir variables
mas = "true"
x1 = 0
x2 = 0
y1 = 0
y2 = 0
while mas == "true":
    if mas == "true":
        x1 = float(input("Ingrese el valor de x1 = "))
        y1 = float(input("Ingrese el valor de y1 = "))
        x2 = float(input("Ingrese el valor de x2 = "))
        y2 = float(input("Ingrese el valor de y2 = "))
        #PROCESO
        d = (pow(x2 - x1, 2) + pow(y2 - y1, 2))**(0.5)
        print("La distancia entre los puntos es = " + str(d) + "\n")
        mas = str(input("¿Quieres seguir calculando la distancia entre dos puntos? true o false = "))