v1 = int(input("Ingrese el primer voltaje\n"))
v2 = int(input("Ingrese el segundo voltaje\n"))
v3 = int(input("Ingrese el tercer voltaje\n"))

promedio = (v1+v2+v3)/3

if promedio < 115:
    print("Voltaje correcto")
elif promedio > 115 and promedio < 220:
    print("Voltaje alto")
else:  
    print("peligro")