import sys

usuarios = []
prestamo = []
bicicletas = ['bicicleta1', 'bicicleta2', 'bicicleta3']

def registrar_usuario():
    print("****************REGISTRO DE USUARIOS****************")
    print("Ingrese el número de la tarjeta")
    usuarios.append(input())
    print("Ingrese el nombre")
    usuarios.append(input())
    print("Ingrese el apellido")
    usuarios.append(input())
    print("Ingrese el correo")
    usuarios.append(input())

def prestar_bicicleta():
    print("****************PRESTAR BICICLETA****************")
    print("Ingrese el número de la tarjeta")
    tarjeta = input()
    if tarjeta in usuarios:
        print("Seleccione el número de la bicicleta:")
        for i, bici in enumerate(bicicletas):
            print(f"{i+1}. {bici}")
        seleccion = int(input()) - 1
        bicicleta_seleccionada = bicicletas[seleccion]

        print("Ingrese el origen")
        origen = input()
        print("Ingrese el destino")
        destino = input()

        prestamo.extend([bicicleta_seleccionada, origen, destino])
        print("Préstamo registrado.")
    else:
        print("La tarjeta no se encuentra registrada, vuelva al menú")

def listar_usuarios():
    print("******************LISTADO DE USUARIOS****************")
    for i in range(0, len(usuarios), 4):
        print(f"Tarjeta: {usuarios[i]}, Nombre: {usuarios[i+1]}, Apellido: {usuarios[i+2]}, Correo: {usuarios[i+3]}")

def listar_prestamos():
    print("********************LISTADO DE PRESTAMOS*************")
    for i in range(0, len(prestamo), 3):
        print(f"Bicicleta: {prestamo[i]}, Origen: {prestamo[i+1]}, Destino: {prestamo[i+2]}")

def menu():
    while True:
        print("Ingrese la opción que desea realizar")
        print("*****Menú****")
        print("opción 1------>Registrar usuario")
        print("opción 2------>Prestar una bicicleta")
        print("opción 3------>Consultar el listado de usuarios")
        print("opción 4------>Consultar el listado de prestamos")

        opcion = int(input())

        if opcion == 1:
            registrar_usuario()
        elif opcion == 2:
            prestar_bicicleta()
        elif opcion == 3:
            listar_usuarios()
        elif opcion == 4:
            listar_prestamos()
        else:
            print("Opción no válida")
            continue

        print("¿Desea realizar otra acción? (1: para volver al menú, cualquier otro número para salir)")
        continuar = int(input())
        if continuar != 1:
            break

    print("Hasta luego")
    sys.exit()

menu()

