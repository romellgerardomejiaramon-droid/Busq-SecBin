
TAMANO = 7


def funcion_hash(clave):
    return clave % TAMANO


def buscar_hash(registros, objetivo):
    tabla = [[] for _ in range(TAMANO)]

    print("\n========== RESOLUCION PASO A PASO ==========")
    print("METODO: BUSQUEDA HASH")
    print("PROBLEMA: Buscar un empleado por identificacion.")

    print("\nPaso 1. Crear tabla hash de 7 posiciones.")

    for i in range(TAMANO):
        print(f"Posicion {i}: vacia")

    print("\nPaso 2. Insertar los empleados.")

    for identificacion, nombre in registros:
        posicion = funcion_hash(identificacion)

        print(f"\nEmpleado: {nombre}")
        print(f"Identificacion: {identificacion}")
        print(f"Calculo: h({identificacion}) = {identificacion} % 7")
        print(f"Posicion calculada: {posicion}")

        if tabla[posicion]:
            print("Colision detectada.")
            print("La posicion ya esta ocupada.")
            print("Se agrega el empleado a la lista existente.")
        else:
            print("La posicion esta libre.")

        tabla[posicion].append((identificacion, nombre))
        print("Contenido de la posicion:", tabla[posicion])

    print("\nPaso 3. Mostrar la tabla hash.")

    for i, cubeta in enumerate(tabla):
        print(f"Posicion {i}: {cubeta}")

    posicion = funcion_hash(objetivo)

    print("\nPaso 4. Calcular la posicion de busqueda.")
    print(f"h({objetivo}) = {objetivo} % 7 = {posicion}")

    print("\nPaso 5. Revisar la cubeta correspondiente.")

    comparaciones = 0
    encontrado = None

    for identificacion, nombre in tabla[posicion]:
        comparaciones += 1

        print(f"\nComparacion {comparaciones}:")
        print("Identificacion almacenada:", identificacion)
        print("Identificacion buscada:", objetivo)

        if identificacion == objetivo:
            print("Las identificaciones coinciden.")
            print("Empleado encontrado.")
            encontrado = (identificacion, nombre)
            break
        else:
            print("No coincide. Continuar con el siguiente registro.")

    print("\n========== RESULTADO FINAL ==========")

    if encontrado:
        print("Nombre del empleado:", encontrado[1])
        print("Identificacion:", encontrado[0])
        print("Posicion hash:", posicion)
    else:
        print("No se encontro al empleado.")

    print("Comparaciones realizadas:", comparaciones)


def principal():
    ejemplo = [
        (201, "Carlos"),
        (208, "Maria"),
        (215, "Jose"),
        (202, "Andrea"),
        (220, "Luis")
    ]

    while True:
        print("\n========== BUSQUEDA HASH DE EMPLEADOS ==========")
        print("1. Resolver ejemplo")
        print("2. Resolver mi propio ejercicio")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            buscar_hash(ejemplo, 208)

        elif opcion == "2":
            try:
                registros = []
                cantidad = int(input("Cuantos empleados deseas registrar? "))

                if cantidad < 1:
                    print("Debes ingresar al menos un empleado.")
                    continue

                for i in range(cantidad):
                    print(f"\nEmpleado {i + 1}")
                    identificacion = int(input("Identificacion: "))
                    nombre = input("Nombre: ").strip()
                    registros.append((identificacion, nombre))

                objetivo = int(input("Identificacion que deseas buscar: "))
                buscar_hash(registros, objetivo)

            except ValueError:
                print("Ingresa identificaciones numericas validas.")

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    principal()
