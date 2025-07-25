lista_productos = []
lista_precios = []


def sumar_productos(total):
    total = 0
    for precio in lista_precios:
        total += precio
    return total


def mostrar_productos(productos, precios):
    if not lista_productos:
        print("No hay productos en la lista.")
    else:
        for producto, precio in zip(lista_productos, lista_precios):
            print(f"Producto: {producto}, Precio: {precio}")


def aplicar_descuento(descuento):
    if lista_productos >= 5:
        print("Aplicando descuento del 20% a todos los productos.")
        for i in range(len(lista_precios)):
            lista_precios[i] -= lista_precios[i] * 0.20
    return descuento


def main():
    while True:
        print("si usted no ingresa nada se saldra del programa")
        producto = input("Ingrese el nombre del producto (o presione Enter para salir): ")
        if producto == "":
            break
        precio = float(input(f"Ingrese el precio del producto '{producto}': "))
        lista_productos.append(producto)
        lista_precios.append(precio)