# Datos constantes
precio_comun = 15000
precio_3d = 20000
precio_xd = 25000

# Datos de salida
suma_edad = 0
total_personas = 0
visitantes_sala_comun = 0
visitantes_sala_3d = 0
visitantes_sala_xd = 0
total_recaudado_comun = 0
total_recaudado_3d = 0
total_recaudado_xd = 0

# Valor de loopeo
sigue_procesando = True
while sigue_procesando:
    procesar = 2
    while procesar != 0 and procesar != 1:
        print("¿Desea cargar una nueva reserva?")
        print("[0] No")
        print("[1] Si")

        procesar = int(input())

        if procesar != 0 and procesar != 1:
            print("Ingrese un valor valido.")

        if procesar == 0:
            sigue_procesando = False
            break

    if not sigue_procesando:
        break

    nombre_reservante = input("Ingrese el nombre del reservante: ")
    edad_reservante = 0
    suma_edad_reserva = 0

    while edad_reservante < 18 or edad_reservante > 100:
        edad_reservante = int(input("Ingrese la edad del reservante: "))
        suma_edad_reserva += edad_reservante

        if edad_reservante < 18 or edad_reservante > 100:
            print("Ingrese una edad valida")

    cantidad_acompanantes = int(input("Ingrese cantidad de acompañantes: "))
    for acompaniante in range(cantidad_acompanantes):
        edad_acompaniante = int(input("Ingrese la edad del acompañante: "))
        suma_edad_reserva += edad_acompaniante

    print("Ingrese el tipo de sala: ")
    print("[1] Común")
    print("[2] 3D")
    print("[3] XD")
    tipo_sala = 0
    while tipo_sala < 1 or tipo_sala > 3:
        tipo_sala = int(input())

        if tipo_sala < 1 or tipo_sala > 3:
            print("Ingrese un valor valido.")

    dia = 0
    while dia < 1 or dia > 7:
        dia = int(input("Ingrese el día que quiere asistir (valor entre 1-7)"))

        if dia < 1 or dia > 7:
            print("Ingrese un valor valido.")

    total_personas_reserva = cantidad_acompanantes + 1
    valor_total = total_personas_reserva

    if dia == 3:
        valor_total /= 2

    match tipo_sala:
        case 1:
            visitantes_sala_comun += 1
            valor_total *= precio_comun
            total_recaudado_comun += valor_total
        case 2:
            visitantes_sala_3d += 1
            valor_total *= precio_3d
            total_recaudado_3d += valor_total
        case 3:
            visitantes_sala_xd += 1
            valor_total *= precio_xd
            total_recaudado_xd += valor_total

    print(f"Edad total de la reserva {suma_edad_reserva}")
    print(f"Total personas de la reserva {total_personas_reserva}")
    print(f"Precio por persona {valor_total}")

    suma_edad += suma_edad_reserva
    total_personas += total_personas_reserva

print("Reservas finalizadas.")
print(f"Suma edad total de todas las reservas {suma_edad}")
print(f"Cantidad total de personas de todas las reservas {total_personas}")
print(f"Recaudado por sala comun {total_recaudado_comun}")
print(f"Recaudado por sala 3D {total_recaudado_3d}")
print(f"Recaudado por sala XD {total_recaudado_xd}")
