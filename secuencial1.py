
def buscar(datos, objetivo):
    print("\n========== RESOLUCION PASO A PASO ==========")
    print("METODO: BUSQUEDA SECUENCIAL")
    print("PROBLEMA: Buscar una ciudad")

    print("\nPaso 1. Lista de ciudades:", datos)
    print("Paso 2. Ciudad que se desea encontrar:", objetivo)
    print("\nPaso 3. Recorrer la lista desde el primer elemento.")

    comparaciones = 0
    encontrado = False

    for i, ciudad in enumerate(datos):
        comparaciones += 1

        print(f"\n--- Iteracion {comparaciones} ---")
        print(f"Posicion revisada: {i}")
        print(f"Ciudad actual: {ciudad}")
        print(f"Operacion: {ciudad.lower()} == {objetivo.lower()}")

        if ciudad.lower() == objetivo.lower():
            print("Resultado de la comparacion: VERDADERO")
            print("La ciudad coincide con la buscada.")
            print("Se detiene el recorrido.")
            encontrado = True
            break
        else:
            print("Resultado de la comparacion: FALSO")
            print("La ciudad no coincide.")
            print("Se avanza a la siguiente posicion.")

    print("\n========== RESULTADO ==========")

    if encontrado:
        print("La ciudad fue encontrada.")
        print("Ciudad:", ciudad)
        print("Posicion comenzando desde 1:", i + 1)
    else:
        print("La ciudad no aparece en la lista.")

    print("Comparaciones realizadas:", comparaciones)
    print("Fin de la resolucion paso a paso.")


def principal():
    datos_ejemplo = ["Merida", "Cancun", "Campeche", "Valladolid", "Progreso"]
    objetivo_ejemplo = "Valladolid"

    while True:
        print("\n========== BUSQUEDA SECUENCIAL DE CIUDADES ==========")
        print("1. Resolver ejemplo")
        print("2. Resolver mi propio ejercicio")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            buscar(datos_ejemplo, objetivo_ejemplo)

        elif opcion == "2":
            datos = [
                ciudad.strip()
                for ciudad in input("Ingresa las ciudades separadas por comas: ").split(",")
                if ciudad.strip()
            ]

            if not datos:
                print("Debes ingresar al menos una ciudad.")
                continue

            objetivo = input("Ciudad que deseas buscar: ").strip()

            if not objetivo:
                print("Debes ingresar una ciudad para buscar.")
                continue

            buscar(datos, objetivo)

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    principal()
