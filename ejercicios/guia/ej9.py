salario = 250000
comision = 50000
numero_vendedor = int(input("Introduce el numero vendedor: "))
cantidad_ventas = int(input("Ingrese la cantidad de ventas: "))
valor_venta = int(input("Ingrese el valor de venta: "))

salario_final = salario + cantidad_ventas * comision + valor_venta * 0.05 * cantidad_ventas
print(f"El salario final del vendedor {numero_vendedor} fue de: {salario_final}")