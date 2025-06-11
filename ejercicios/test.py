conteo = 0
quiere_seguir_contando = True
while quiere_seguir_contando:
    print(conteo)
    conteo = conteo + 1
    quiere_seguir_contando = bool(input("Ingrese 1 si quiere seguir contando, 0 si no."))
    print(quiere_seguir_contando)
