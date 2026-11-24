
def buscar_libro(libros, codigo):
    print("\n========== RESOLUCION PASO A PASO ==========")
    print("METODO: BUSQUEDA BINARIA")
    print("\nPaso 1. Mostrar los libros originales:")

    for libro in libros:
        print(f"Codigo: {libro[0]} | Nombre: {libro[1]}")

    libros = sorted(libros, key=lambda libro: libro[0])

    print("\nPaso 2. Ordenar los libros por codigo:")
    for libro in libros:
        print(f"Codigo: {libro[0]} | Nombre: {libro[1]}")

    print("\nPaso 3. Codigo que se desea buscar:", codigo)

    izquierda = 0
    derecha = len(libros) - 1
    comparaciones = 0
    paso = 1
    encontrado = None

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = libros[medio]
        comparaciones += 1

        print(f"\n========== PASO {paso} ==========")
        print(f"Limite izquierdo: {izquierda}")
        print(f"Limite derecho: {derecha}")
        print(f"Centro = ({izquierda} + {derecha}) // 2 = {medio}")
        print(f"Libro central: {actual[1]}")
        print(f"Codigo central: {actual[0]}")
        print(f"Comparacion: {actual[0]} == {codigo}")

        if actual[0] == codigo:
            print("El codigo coincide.")
            print("Libro encontrado.")
            encontrado = actual
            break

        elif actual[0] < codigo:
            print("El codigo central es menor que el buscado.")
            print("Se descarta la mitad izquierda.")
            izquierda = medio + 1
            print("Nuevo limite izquierdo:", izquierda)

        else:
            print("El codigo central es mayor que el buscado.")
            print("Se descarta la mitad derecha.")
            derecha = medio - 1
            print("Nuevo limite derecho:", derecha)

        paso += 1

    print("\n========== RESULTADO FINAL ==========")

    if encontrado:
        print("Libro encontrado:", encontrado[1])
        print("Codigo:", encontrado[0])
        print("Posicion en lista ordenada:", medio + 1)
    else:
        print("No se encontro el libro.")

    print("Total de comparaciones:", comparaciones)


def principal():
    ejemplo = [
        (105, "Matematicas"),
        (101, "Programacion"),
        (104, "Bases de datos"),
        (102, "Estructuras de datos"),
        (103, "Redes")
    ]

    while True:
        print("\n========== BUSQUEDA BINARIA DE LIBROS ==========")
        print("1. Resolver ejemplo")
        print("2. Resolver mi propio ejercicio")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            buscar_libro(ejemplo, 104)

        elif opcion == "2":
            try:
                libros = []
                cantidad = int(input("Cuantos libros deseas registrar? "))

                if cantidad < 1:
                    print("Debes registrar al menos un libro.")
                    continue

                for i in range(cantidad):
                    print(f"\nRegistro del libro {i + 1}")
                    codigo = int(input("Codigo: "))
                    nombre = input("Nombre: ").strip()
                    libros.append((codigo, nombre))

                codigo_buscar = int(input("Codigo que deseas buscar: "))
                buscar_libro(libros, codigo_buscar)

            except ValueError:
                print("Ingresa datos validos.")

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    principal()
