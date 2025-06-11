# CONDICIONALES
seguir_preguntando = True

# CONTADORES
cantidad_reservas_sala_peque = 0
cantidad_reservas_sala_media = 0
cantidad_reservas_sala_grande = 0

# ACUMULADORES
monto_total_reservas_sala_peque = 0
monto_total_reservas_sala_media = 0
monto_total_reservas_sala_grande = 0

while seguir_preguntando:
    numero_reserva = int(input("Ingrese el número de reserva. Ingrese -1 para finalizar:"))
    if numero_reserva == -1:
        seguir_preguntando = False
    else:
        if numero_reserva < 1000 or numero_reserva > 9999:
            print("Ingrese un número de reserva valido.")
        else:
            edad = 0
            while 21 > edad > 65:
                edad = int(input("Ingrese su edad: "))

                if 21 > edad > 65:
                    print("Edad no valida. Por favor intente nuevamente.")
            
            cantidad_horas = int(input("Ingrese la cantidad de horas que desea reservar la sala: "))
            costo_total_reserva = 0
            cantidad_personas_reserva = 0

            reserva_valida = False
            while not reserva_valida:
                cantidad_personas_reserva = int(input("Ingrese la cantidad de personas para la reserva: "))
                print("Seleccione una sala: ")
                print("[1] para sala pequeña")
                print("[2] para sala mediana")
                print("[3] para sala grande")
                sala_reservada = int(input())
                
                if sala_reservada >= 1 or sala_reservada <= 3:
                    if sala_reservada == 1:
                        if cantidad_personas_reserva > 10:
                            print("Limite excedido.")
                        else:
                            costo_total_reserva = cantidad_horas * 1500
                            monto_total_reservas_sala_peque += costo_total_reserva
                            cantidad_reservas_sala_peque += 1
                            reserva_valida = True
                    elif sala_reservada == 2:
                        if cantidad_personas_reserva > 20:
                            print("Límite excedido.")
                        else:
                            costo_total_reserva = cantidad_horas * 2500
                            monto_total_reservas_sala_media += costo_total_reserva
                            cantidad_reservas_sala_media += 1
                            reserva_valida = True
                    elif sala_reservada == 3:
                        if cantidad_personas_reserva > 50:
                            print("Límite excedido.")
                        else:
                            costo_total_reserva = cantidad_horas * 4000
                            monto_total_reservas_sala_grande += costo_total_reserva
                            cantidad_reservas_sala_grande += 1
                            reserva_valida = True
                else:
                    print("Por favor, ingrese un tipo de sala valido.")

            print(f"Cada persona debera abonar {costo_total_reserva / cantidad_personas_reserva}")

print(f"La sala pequeña ha sido reservada un total de {cantidad_reservas_sala_peque} veces y ha recaudado {monto_total_reservas_sala_peque}$")
print(f"La sala media ha sido reservada un total de {cantidad_reservas_sala_media} veces y ha recaudado {monto_total_reservas_sala_media}$")
print(f"La sala grande ha sido reservada un total de {cantidad_reservas_sala_grande} veces y ha recaudado {monto_total_reservas_sala_grande}$")

if cantidad_reservas_sala_peque == cantidad_reservas_sala_media == cantidad_reservas_sala_grande:
    print("Todas fueron reservadas por igual.")
else:
    if cantidad_reservas_sala_peque >= cantidad_reservas_sala_media and cantidad_reservas_sala_peque >= cantidad_reservas_sala_grande:
        if cantidad_reservas_sala_peque == cantidad_reservas_sala_media:
            print("La sala pequeña y la media fueron las más reservadas.")
        elif cantidad_reservas_sala_peque == cantidad_reservas_sala_grande:
            print("La sala pequeña y la grande fueron las más reservadas.")
        else:
            print("La sala pequeña fue la más reservada.")
    elif cantidad_reservas_sala_media >= cantidad_reservas_sala_peque and cantidad_reservas_sala_media >= cantidad_reservas_sala_grande:
        if cantidad_reservas_sala_media == cantidad_reservas_sala_grande:
            print("La sala media y la grande fueron las más reservadas.")
        else:
            print("La sala media fue la más reservada.")
    else:
        print("La sala grande fue la más reservada.")

total_reservas = cantidad_reservas_sala_peque + cantidad_reservas_sala_media + cantidad_reservas_sala_grande
print(f"Total reservas: {total_reservas}")
print(f"Procentaje sala pequeña: {cantidad_reservas_sala_peque/total_reservas * 100}")
print(f"Procentaje sala media: {cantidad_reservas_sala_media/total_reservas * 100}")
print(f"Procentaje sala grande: {cantidad_reservas_sala_grande/total_reservas * 100}")
