
TAMANO = 7


def funcion_hash(clave):
    return clave % TAMANO


def buscar_hash(registros, objetivo):
    tabla = [[] for _ in range(TAMANO)]

    print("\n========== RESOLUCION PASO A PASO ==========")
    print("METODO: BUSQUEDA HASH")
    print("PROBLEMA: Buscar un producto por codigo.")
    print("\nPaso 1. Crear una tabla hash de 7 posiciones.")

    for i in range(TAMANO):
        print(f"Posicion {i}: vacia")

    print("\nPaso 2. Insertar los productos.")

    for clave, nombre in registros:
        posicion = funcion_hash(clave)

        print(f"\nInsertar producto: {nombre}")
        print(f"Codigo: {clave}")
        print(f"Funcion hash: h({clave}) = {clave} % 7")
        print(f"Resultado: {posicion}")

        if tabla[posicion]:
            print("Se produce una colision.")
            print("La posicion ya contiene otro producto.")
            print("Se agrega el nuevo producto a la misma lista.")
        else:
            print("La posicion esta disponible.")

        tabla[posicion].append((clave, nombre))
        print(f"Contenido actual de la posicion {posicion}: {tabla[posicion]}")

    print("\nPaso 3. Mostrar la tabla hash completa.")

    for i, cubeta in enumerate(tabla):
        print(f"Posicion {i}: {cubeta}")

    posicion = funcion_hash(objetivo)

    print("\nPaso 4. Calcular la posicion de busqueda.")
    print(f"h({objetivo}) = {objetivo} % 7 = {posicion}")

    print(f"\nPaso 5. Revisar solamente la posicion {posicion}.")

    comparaciones = 0
    encontrado = None

    for clave, nombre in tabla[posicion]:
        comparaciones += 1

        print(f"\nComparacion {comparaciones}:")
        print(f"Codigo almacenado: {clave}")
        print(f"Codigo buscado: {objetivo}")

        if clave == objetivo:
            print("Los codigos coinciden.")
            print("Producto encontrado.")
            encontrado = (clave, nombre)
            break
        else:
            print("Los codigos son diferentes.")
            print("Se revisa el siguiente elemento de la misma posicion.")

    print("\n========== RESULTADO FINAL ==========")

    if encontrado:
        print("Producto:", encontrado[1])
        print("Codigo:", encontrado[0])
        print("Posicion hash:", posicion)
    else:
        print("No se encontro el producto.")

    print("Comparaciones realizadas:", comparaciones)


def principal():
    ejemplo = [
        (101, "Teclado"),
        (108, "Mouse"),
        (115, "Monitor"),
        (102, "Audifonos"),
        (120, "Bocinas")
    ]

    while True:
        print("\n========== BUSQUEDA HASH DE PRODUCTOS ==========")
        print("1. Resolver ejemplo")
        print("2. Resolver mi propio ejercicio")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            buscar_hash(ejemplo, 115)

        elif opcion == "2":
            try:
                registros = []
                cantidad = int(input("Cuantos productos deseas registrar? "))

                if cantidad < 1:
                    print("Debes ingresar al menos un producto.")
                    continue

                for i in range(cantidad):
                    print(f"\nProducto {i + 1}")
                    clave = int(input("Codigo: "))
                    nombre = input("Nombre: ").strip()
                    registros.append((clave, nombre))

                objetivo = int(input("Codigo que deseas buscar: "))
                buscar_hash(registros, objetivo)

            except ValueError:
                print("Ingresa codigos numericos validos.")

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    principal()
