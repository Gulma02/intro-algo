end = False
par_o_impar = True
while not end:
    numero = int(input("Introduce un numero"))

    if numero == -1:
        end = True
        continue

    par_o_impar = not par_o_impar


if (par_o_impar):
    print("Par!")
else:
    print("Impar!")