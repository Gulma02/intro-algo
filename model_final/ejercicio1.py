lista_clientes = []
lista_horarios = []

def agregar_cliente(nuevo_cliente, nuevo_horario):
    lista_clientes.append(nuevo_cliente)
    lista_horarios.append(nuevo_horario)

    print("Cliente registrado con exito.")

def validar_cliente_registardo(cliente_a_validar):
    if cliente_a_validar in lista_clientes:
        print("Cliente ya registrado. Ingrese otro cliente.")
        return ""

    if cliente_a_validar == "":
        print("Ingrese un nombre valido.")
        return ""

    return cliente_a_validar

def ordenar_horarios():
    for i in range(len(lista_horarios)):
        for j in range(i + 1, len(lista_horarios)):
            if lista_horarios[i] > lista_horarios[j]:
                lista_horarios[i], lista_horarios[j] = lista_horarios[j], lista_horarios[i]
                lista_clientes[i], lista_clientes[j] = lista_clientes[j], lista_clientes[i]

def mostrar_horarios():
    for i in range(len(lista_horarios)):
        print(f"Horario: {lista_horarios[i]} - Cliente: {lista_clientes[i]}")

def buscar_turno(para_cliente):
    if para_cliente in lista_clientes:
        for i in range(len(lista_clientes)):
            if lista_clientes[i] == para_cliente:
                print(f"{lista_clientes[i]} tiene un turno a las {lista_horarios[i]}")
    else:
        print("Cliente no se encuentra registrado.")
        return ""

execute = True
cargar_horarios = 0
while not cargar_horarios == -1:
    cargar_horarios = int(input("Ingrese 1 para cargar nuevo horario, -1 para finalizar: "))
    match cargar_horarios:
        case 1:
            cliente = ""
            while cliente == "":
                cliente = validar_cliente_registardo(input("Ingrese el nombre del cliente: "))

            horario = input("Ingrese el horario: ")
            agregar_cliente(cliente, horario)

ordenar_horarios()
mostrar_horarios()

while execute:
    buscar_turno(input("Ingrese el nombre del cliente a buscar turno: "))
