
def buscar_binaria(datos, objetivo):
    print("\n========== RESOLUCION PASO A PASO ==========")
    print("METODO: BUSQUEDA BINARIA")
    print("\nPaso 1. Matriculas originales:", datos)

    datos = sorted(datos)
    print("Paso 2. Ordenar las matriculas:", datos)
    print("Paso 3. Matricula que se desea buscar:", objetivo)

    izquierda = 0
    derecha = len(datos) - 1
    comparaciones = 0
    paso = 1
    encontrado = False

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        matricula = datos[medio]
        comparaciones += 1

        print(f"\n========== PASO {paso} ==========")
        print(f"Limite izquierdo: {izquierda}")
        print(f"Limite derecho: {derecha}")
        print(f"Centro = ({izquierda} + {derecha}) // 2 = {medio}")
        print("Matricula central:", matricula)
        print(f"Comparacion: {matricula} == {objetivo}")

        if matricula == objetivo:
            print("La matricula coincide con la buscada.")
            encontrado = True
            break

        elif matricula < objetivo:
            print("La matricula central es menor que la buscada.")
            print("Se descarta la mitad izquierda.")
            izquierda = medio + 1
            print("Nuevo limite izquierdo:", izquierda)

        else:
            print("La matricula central es mayor que la buscada.")
            print("Se descarta la mitad derecha.")
            derecha = medio - 1
            print("Nuevo limite derecho:", derecha)

        paso += 1

    print("\n========== RESULTADO FINAL ==========")

    if encontrado:
        print("Matricula encontrada:", matricula)
        print("Posicion en la lista ordenada:", medio + 1)
    else:
        print("La matricula no se encuentra.")

    print("Total de comparaciones:", comparaciones)


def principal():
    ejemplo = [1050, 1010, 1040, 1020, 1030, 1060]

    while True:
        print("\n========== BUSQUEDA BINARIA DE MATRICULAS ==========")
        print("1. Resolver ejemplo")
        print("2. Resolver mi propio ejercicio")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            buscar_binaria(ejemplo, 1040)

        elif opcion == "2":
            try:
                datos = [
                    int(x.strip())
                    for x in input("Ingresa matriculas separadas por comas: ").split(",")
                ]

                if not datos:
                    print("Debes ingresar matriculas.")
                    continue

                objetivo = int(input("Matricula que deseas buscar: "))
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
