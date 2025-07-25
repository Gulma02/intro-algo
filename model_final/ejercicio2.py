lista_productos = []
lista_precios = []

def visualizar_productos():
    for producto in range(len(lista_productos)): # Donde inicia y donde finaliza
        print(f"El producto {lista_productos[producto]} cuesta {lista_precios[producto]}$")

def calcular_total_a_pagar():
    # Validar si la lista tiene más de 5 productos
    # Si tiene más de 5, aplicar 20% off
    total_precio = 0

    for i in range(len(lista_precios)):
        total_precio += lista_precios[i]

    if len(lista_precios) >= 5:
        print("El descuento total fue de: ", total_precio * 0.2)

        total_precio *= 0.8

    return total_precio

def cargar_producto(producto, precio):
    lista_productos.append(producto)
    lista_precios.append(precio)

nuevo_producto = "a"
while not nuevo_producto == "":
    nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
    if nuevo_producto == "":
        break

    cargar_producto(nuevo_producto, int(input("Ingrese el precio del nuevo producto: ")))

visualizar_productos()
print(f"El total a pagar es de: {calcular_total_a_pagar()}")