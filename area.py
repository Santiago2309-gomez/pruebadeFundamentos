#area=base*altura/2
base = int(input("Ingrese la base"))
altura = int (input("Ingrese la altura"))

area = (base*altura)/2

if area > 1000:
    print ("Datos no validos")
else:
    print (f"El area del triangulo es {area}")

