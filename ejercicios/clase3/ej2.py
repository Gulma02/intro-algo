ejuan = int(input("Ingrese la edad de Juan: "))
emario = int(input("Ingrese la edad de Mario: "))
epedro = int(input("Ingrese la edad de Pedro: "))

if ejuan == emario == epedro:
    print("Todos son contemporaneos")
elif ejuan == emario:
    print("Juan y Mario son contemporaneos")
elif ejuan == epedro:
    print("Juan y Pedro son contemporaneos")
elif emario == epedro:
    print("Juan y Pedro son contemporaneos")
else:
    print("Nadie es contemporaneo")