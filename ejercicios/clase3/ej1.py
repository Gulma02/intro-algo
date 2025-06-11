monto = int(input("Ingrese el valor del producto: "))
tipo_pago = 0

while tipo_pago != 1 and tipo_pago != 2:
    tipo_pago = int(input("Ingrese el tipo de pago. [1] Tarjeta de credito [2] Tarjeta de debito. "))

    if tipo_pago != 1 and tipo_pago != 2:
        print("Tipo de pago incorrecto. Por favor ingrese un valor valido")


if tipo_pago == 1:
    monto += monto * 20 / 100

print(f"Su monto es: {monto}")