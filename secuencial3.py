
def buscar(datos, objetivo):
    print("\n========== RESOLUCION PASO A PASO ==========")
    print("METODO: BUSQUEDA SECUENCIAL")
    print("PROBLEMA: Buscar una calificacion")

    print("\nPaso 1. Mostrar las calificaciones:")
    for i, calificacion in enumerate(datos):
        print(f"Posicion {i + 1}: {calificacion}")

    print("\nPaso 2. Calificacion que se desea encontrar:", objetivo)
    print("Paso 3. Comenzar la busqueda desde la primera posicion.")

    comparaciones = 0
    encontrado = False

    for i, calificacion in enumerate(datos):
        comparaciones += 1

        print(f"\n--- Iteracion {comparaciones} ---")
        print(f"Calificacion actual: {calificacion}")
        print(f"Operacion: {calificacion} == {objetivo}")

        if calificacion == objetivo:
            print("Resultado: VERDADERO")
            print("La calificacion coincide.")
            print("Se termina el recorrido.")
            encontrado = True
            break
        else:
            print("Resultado: FALSO")
            print("La calificacion no coincide.")
            print("Se revisa la siguiente posicion.")

    print("\n========== RESULTADO ==========")

    if encontrado:
        print("Calificacion encontrada:", calificacion)
        print("Posicion comenzando desde 1:", i + 1)
    else:
        print("La calificacion no se encuentra en la lista.")

    print("Comparaciones realizadas:", comparaciones)
    print("Fin de la resolucion paso a paso.")


def principal():
    datos_ejemplo = [85, 90, 75, 100, 88]
    objetivo_ejemplo = 100

    while True:
        print("\n========== BUSQUEDA SECUENCIAL DE CALIFICACIONES ==========")
        print("1. Resolver ejemplo")
        print("2. Resolver mi propio ejercicio")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            buscar(datos_ejemplo, objetivo_ejemplo)

        elif opcion == "2":
            try:
                datos = [
                    float(x.strip())
                    for x in input("Ingresa las calificaciones separadas por comas: ").split(",")
                ]

                if not datos:
                    print("Debes ingresar al menos una calificacion.")
                    continue

                objetivo = float(input("Calificacion que deseas buscar: "))
                buscar(datos, objetivo)

            except ValueError:
                print("Ingresa solamente valores numericos.")

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    principal()
