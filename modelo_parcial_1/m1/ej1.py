num_reserva = 0
cantidad_reservas_mesa_1 = 0
cantidad_reservas_mesa_2 = 0
cantidad_reservas_mesa_3 = 0
monto_total_mesa_1 = 0
monto_total_mesa_2 = 0
monto_total_mesa_3 = 0

while num_reserva != -1:
    while num_reserva < 1000 or num_reserva > 9999:
        num_reserva = int(input("Ingrese el número de reserva: "))

        if num_reserva == -1:
            break

        if num_reserva < 1000 or num_reserva > 9999:
            print("Número de reserva invalido. Por favor ingrese un valor valido.")

    if num_reserva == -1:
        break

    print("Mesa reservada")

    edad = 0
    while edad < 18 or edad > 65:
        edad = int(input("Ingrese su edad: "))

        if edad < 18 or edad > 65:
            print("Edad invalida. Por favor ingrese una edad valida.")

    cantidad_personas = 0
    while cantidad_personas < 1 or cantidad_personas > 12:
        cantidad_personas = int(input("Ingrese la cantidad de personas: "))

        if cantidad_personas < 1 or cantidad_personas > 12:
            print("Cantidad de personas invalida. Por favor ingrese un valor valido.")

    mesa_seleccionada = 0
    precio_mesa = 0

    while mesa_seleccionada < 1 or mesa_seleccionada > 3:
        print("Elija un tipo de mesa: ")
        print()
        print("[1] Mesa para 2 a 4 personas")
        print("[2] Mesa para 5 a 8 personas")
        print("[3] Mesa para 9 a 12 personas")
        print()

        mesa_seleccionada = int(input("Ingrese que tipo de mesa quiere: "))

        if mesa_seleccionada < 1 or mesa_seleccionada > 3:
            print("Tipo de mesa invalido. Por favor vuelva a ingresar el tipo de mesa.")
        else:
            match mesa_seleccionada:
                case 1:
                    if cantidad_personas < 2 or cantidad_personas > 4:
                        print("Usted no puede usar este tipo de mesa. Seleccione una acorde")
                        mesa_seleccionada = 0
                    else:
                        precio_mesa = 1000
                        cantidad_reservas_mesa_1 += 1
                case 2:
                    if cantidad_personas < 5 or cantidad_personas > 8:
                        print("Usted no puede usar este tipo de mesa. Seleccione una acorde")
                        mesa_seleccionada = 0
                    else:
                        precio_mesa = 1800
                        cantidad_reservas_mesa_2 += 1
                case 3:
                    if cantidad_personas < 9 or cantidad_personas > 12:
                        print("Usted no puede usar este tipo de mesa. Seleccione una acorde")
                        mesa_seleccionada = 0
                    else:
                        precio_mesa = 2500
                        cantidad_reservas_mesa_3 += 1

    total_gastado = int(input("Ingrese el monto total gastado: "))

    match mesa_seleccionada:
        case 1:
            total_gastado += precio_mesa * cantidad_personas
            monto_total_mesa_1 += total_gastado
        case 2:
            total_gastado += precio_mesa * cantidad_personas
            monto_total_mesa_2 += total_gastado
        case 3:
            total_gastado += precio_mesa * cantidad_personas
            monto_total_mesa_3 += total_gastado

    print(f"Cada uno debe abonar: {total_gastado / cantidad_personas}")
    print()
    num_reserva = 0

print(f"La mesa número 1 ha recaudado: {monto_total_mesa_1}")
print(f"La mesa número 2 ha recaudado: {monto_total_mesa_2}")
print(f"La mesa número 3 ha recaudado: {monto_total_mesa_3}")

if cantidad_reservas_mesa_1 >= cantidad_reservas_mesa_2 and cantidad_reservas_mesa_1 >= cantidad_reservas_mesa_3:
    print("La mesa 1 fue la más reservada")
    if cantidad_reservas_mesa_1 > cantidad_reservas_mesa_2 and cantidad_reservas_mesa_1 > cantidad_reservas_mesa_3:
        if cantidad_reservas_mesa_2 == cantidad_reservas_mesa_3:
            print("Las mesas 2 y 3 tuvieron la misma cantidad de reservas")
    else:
        if cantidad_reservas_mesa_1 == cantidad_reservas_mesa_2:
            print("Junto a la mesa 2")
        if cantidad_reservas_mesa_1 == cantidad_reservas_mesa_3:
            print("Junto a la mesa 3")
elif cantidad_reservas_mesa_2 >= cantidad_reservas_mesa_1 and cantidad_reservas_mesa_2 >= cantidad_reservas_mesa_3:
    print("La mesa 2 fue la más reservada")
    if cantidad_reservas_mesa_2 > cantidad_reservas_mesa_1 and cantidad_reservas_mesa_2 > cantidad_reservas_mesa_3:
        if cantidad_reservas_mesa_1 == cantidad_reservas_mesa_3:
            print("Las mesas 1 y 3 tuvieron la misma cantidad de reservas")
    else:
        if cantidad_reservas_mesa_2 == cantidad_reservas_mesa_1:
            print("Junto a la mesa 1")

        if cantidad_reservas_mesa_2 == cantidad_reservas_mesa_3:
            print("Junto a la mesa 3")
elif cantidad_reservas_mesa_3 >= cantidad_reservas_mesa_1 and cantidad_reservas_mesa_3 >= cantidad_reservas_mesa_2:
    print("La mesa 3 fue la más reservada")
    if cantidad_reservas_mesa_3 > cantidad_reservas_mesa_1 and cantidad_reservas_mesa_3 > cantidad_reservas_mesa_2:
        if cantidad_reservas_mesa_1 == cantidad_reservas_mesa_2:
            print("Las mesas 1 y 2 tuvieron la misma cantidad de reservas")
    else:
        if cantidad_reservas_mesa_3 == cantidad_reservas_mesa_1:
            print("Junto a la mesa 1")

        if cantidad_reservas_mesa_3 == cantidad_reservas_mesa_2:
            print("Junto a la mesa 2")

cantidad_reservas_totales = cantidad_reservas_mesa_1 + cantidad_reservas_mesa_2 + cantidad_reservas_mesa_3

print(f"Total reservas: {cantidad_reservas_totales}")

print(f"Porcentaje reservas mesa 1: {cantidad_reservas_mesa_1 / cantidad_reservas_totales * 100}%")
print(f"Porcentaje reservas mesa 2: {cantidad_reservas_mesa_2 / cantidad_reservas_totales * 100}%")
print(f"Porcentaje reservas mesa 3: {cantidad_reservas_mesa_3 / cantidad_reservas_totales * 100}%")
