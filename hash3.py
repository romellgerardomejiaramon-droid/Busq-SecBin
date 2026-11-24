
TAMANO = 7


def funcion_hash(clave):
    suma = 0

    for caracter in str(clave):
        suma += ord(caracter)

    return suma % TAMANO


def buscar_hash(registros, objetivo):
    tabla = [[] for _ in range(TAMANO)]

    print("\n========== RESOLUCION PASO A PASO ==========")
    print("METODO: BUSQUEDA HASH")
    print("PROBLEMA: Buscar un contacto por telefono.")

    print("\nPaso 1. Crear una tabla hash de 7 posiciones.")

    for i in range(TAMANO):
        print(f"Posicion {i}: vacia")

    print("\nPaso 2. Insertar los contactos.")

    for telefono, nombre in registros:
        suma = sum(ord(c) for c in telefono)
        posicion = funcion_hash(telefono)

        print(f"\nContacto: {nombre}")
        print("Telefono:", telefono)
        print("Paso de calculo: sumar el valor de cada caracter.")

        for caracter in telefono:
            print(f"Valor de {caracter}: {ord(caracter)}")

        print("Suma total:", suma)
        print(f"Funcion hash: {suma} % {TAMANO} = {posicion}")

        if tabla[posicion]:
            print("Se produce una colision.")
            print("La posicion ya tiene otro contacto.")
            print("Se agrega el contacto a la misma lista.")
        else:
            print("La posicion esta disponible.")

        tabla[posicion].append((telefono, nombre))
        print("Contenido de la posicion:", tabla[posicion])

    print("\nPaso 3. Mostrar la tabla hash.")

    for i, cubeta in enumerate(tabla):
        print(f"Posicion {i}: {cubeta}")

    posicion = funcion_hash(objetivo)

    print("\nPaso 4. Calcular la posicion del telefono buscado.")
    print("Telefono buscado:", objetivo)
    print("Suma de sus caracteres:", sum(ord(c) for c in objetivo))
    print(f"Posicion: {sum(ord(c) for c in objetivo)} % {TAMANO} = {posicion}")

    print(f"\nPaso 5. Revisar la posicion {posicion}.")

    comparaciones = 0
    encontrado = None

    for telefono, nombre in tabla[posicion]:
        comparaciones += 1

        print(f"\nComparacion {comparaciones}:")
        print("Telefono almacenado:", telefono)
        print("Telefono buscado:", objetivo)

        if telefono == objetivo:
            print("Los telefonos coinciden.")
            print("Contacto encontrado.")
            encontrado = (telefono, nombre)
            break
        else:
            print("No coincide. Se revisa el siguiente contacto.")

    print("\n========== RESULTADO FINAL ==========")

    if encontrado:
        print("Nombre:", encontrado[1])
        print("Telefono:", encontrado[0])
        print("Posicion hash:", posicion)
    else:
        print("No se encontro el contacto.")

    print("Comparaciones realizadas:", comparaciones)


def principal():
    ejemplo = [
        ("9991234567", "Carlos"),
        ("9992345678", "Maria"),
        ("9993456789", "Andrea"),
        ("9994567890", "Luis"),
        ("9995678901", "Jose")
    ]

    while True:
        print("\n========== BUSQUEDA HASH DE CONTACTOS ==========")
        print("1. Resolver ejemplo")
        print("2. Resolver mi propio ejercicio")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            buscar_hash(ejemplo, "9993456789")

        elif opcion == "2":
            registros = []

            try:
                cantidad = int(input("Cuantos contactos deseas registrar? "))

                if cantidad < 1:
                    print("Debes ingresar al menos un contacto.")
                    continue

                valido = True

                for i in range(cantidad):
                    print(f"\nContacto {i + 1}")
                    telefono = input("Telefono: ").strip()
                    nombre = input("Nombre: ").strip()

                    if not telefono.isdigit():
                        print("El telefono debe contener solamente digitos.")
                        valido = False
                        break

                    registros.append((telefono, nombre))

                if valido:
                    objetivo = input("Telefono que deseas buscar: ").strip()

                    if objetivo.isdigit():
                        buscar_hash(registros, objetivo)
                    else:
                        print("El telefono debe contener solamente digitos.")

            except ValueError:
                print("Ingresa una cantidad valida.")

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    principal()
