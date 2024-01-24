v1 = int(input("Ingrese el primer voltaje\n"))
v2 = int(input("Ingrese el segundo voltaje\n"))
v3 = int(input("Ingrese el tercer voltaje\n"))
v4 = int(input("Ingrese el cuarto voltaje\n"))
v5 = int(input("Ingrese el quinto voltaje\n"))

prom = (v1+v2+v3+v4+v5)/5

if prom > 258:
    print (f"voltaje alto {prom} voltios")
else:
    print(f"el voltaje {prom} voltios es correcto")