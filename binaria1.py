
def buscar_binaria(datos, objetivo):
    print("\n========== RESOLUCION PASO A PASO ==========")
    print("METODO: BUSQUEDA BINARIA")
    print("\nPaso 1. Datos originales:", datos)

    datos = sorted(datos)
    print("Paso 2. Ordenar los datos de menor a mayor:", datos)
    print("Paso 3. Buscar el numero:", objetivo)

    izquierda = 0
    derecha = len(datos) - 1
    comparaciones = 0
    paso = 1
    encontrado = False

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = datos[medio]
        comparaciones += 1

        print(f"\n========== PASO {paso} ==========")
        print(f"Limite izquierdo: {izquierda}")
        print(f"Limite derecho: {derecha}")
        print(f"Calculo del centro: ({izquierda} + {derecha}) // 2")
        print(f"Centro: {medio}")
        print(f"Valor central: {actual}")
        print(f"Comparacion: {actual} == {objetivo}")

        if actual == objetivo:
            print("El valor central es igual al buscado.")
            print("El numero fue encontrado.")
            encontrado = True
            break

        elif actual < objetivo:
            print(f"{actual} es menor que {objetivo}.")
            print("Se descarta la mitad izquierda.")
            izquierda = medio + 1
            print("Nuevo limite izquierdo:", izquierda)

        else:
            print(f"{actual} es mayor que {objetivo}.")
            print("Se descarta la mitad derecha.")
            derecha = medio - 1
            print("Nuevo limite derecho:", derecha)

        paso += 1

    print("\n========== RESULTADO FINAL ==========")

    if encontrado:
        print("Numero encontrado:", actual)
        print("Posicion en la lista ordenada:", medio + 1)
    else:
        print("El numero no se encuentra en la lista.")

    print("Total de comparaciones:", comparaciones)


def principal():
    ejemplo = [45, 10, 30, 20, 50, 40, 60]

    while True:
        print("\n========== BUSQUEDA BINARIA DE NUMEROS ==========")
        print("1. Resolver ejemplo")
        print("2. Resolver mi propio ejercicio")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            buscar_binaria(ejemplo, 40)

        elif opcion == "2":
            try:
                datos = [
                    int(x.strip())
                    for x in input("Ingresa numeros separados por comas: ").split(",")
                ]

                if not datos:
                    print("Debes ingresar numeros.")
                    continue

                objetivo = int(input("Numero que deseas buscar: "))
                buscar_binaria(datos, objetivo)

            except ValueError:
                print("Ingresa solamente numeros enteros.")

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    principal()
