
def buscar(datos, objetivo):
    print("\n========== RESOLUCION PASO A PASO ==========")
    print("METODO: BUSQUEDA SECUENCIAL")
    print("PROBLEMA: Buscar una matricula")
    print("\nPaso 1. Lista de matriculas:", datos)
    print("Paso 2. Matricula que se desea encontrar:", objetivo)
    print("\nPaso 3. Recorrer la lista desde el primer elemento.")

    comparaciones = 0
    encontrado = False

    for i, matricula in enumerate(datos):
        comparaciones += 1

        print(f"\n--- Iteracion {comparaciones} ---")
        print(f"Posicion revisada: {i}")
        print(f"Matricula actual: {matricula}")
        print(f"Operacion: {matricula} == {objetivo}")

        if matricula == objetivo:
            print("Resultado de la comparacion: VERDADERO")
            print("La matricula coincide con la buscada.")
            print("Se detiene el recorrido.")
            encontrado = True
            break
        else:
            print("Resultado de la comparacion: FALSO")
            print("La matricula no coincide.")
            print("Se avanza a la siguiente posicion.")

    print("\n========== RESULTADO ==========")

    if encontrado:
        print("La matricula fue encontrada.")
        print("Matricula:", matricula)
        print("Posicion comenzando desde 1:", i + 1)
    else:
        print("La matricula no aparece en la lista.")

    print("Comparaciones realizadas:", comparaciones)
    print("Fin de la resolucion paso a paso.")


def principal():
    datos_ejemplo = [1025, 1030, 1012, 1045, 1050]
    objetivo_ejemplo = 1045

    while True:
        print("\n========== BUSQUEDA SECUENCIAL DE ALUMNOS ==========")
        print("1. Resolver ejemplo")
        print("2. Resolver mi propio ejercicio")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            buscar(datos_ejemplo, objetivo_ejemplo)

        elif opcion == "2":
            try:
                datos = [
                    int(x.strip())
                    for x in input("Ingresa las matriculas separadas por comas: ").split(",")
                ]

                if not datos:
                    print("Debes ingresar al menos una matricula.")
                    continue

                objetivo = int(input("Matricula que deseas buscar: "))
                buscar(datos, objetivo)

            except ValueError:
                print("Ingresa solamente numeros enteros.")

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    principal()
