
def buscar(datos, objetivo):
    print("\n========== RESOLUCION PASO A PASO ==========")
    print("METODO: BUSQUEDA SECUENCIAL")
    print("PROBLEMA: Buscar un producto")

    print("\nPaso 1. Lista de productos:")
    for i, producto in enumerate(datos):
        print(f"Posicion {i + 1}: {producto}")

    print("\nPaso 2. Producto que se desea buscar:", objetivo)
    print("Paso 3. Comparar el producto buscado con cada elemento.")

    comparaciones = 0
    encontrado = False

    for i, producto in enumerate(datos):
        comparaciones += 1

        print(f"\n--- Iteracion {comparaciones} ---")
        print(f"Producto actual: {producto}")
        print(f"Operacion: '{producto}' == '{objetivo}'")

        if producto.lower() == objetivo.lower():
            print("Resultado: VERDADERO")
            print("Los nombres coinciden.")
            print("Se detiene la busqueda.")
            encontrado = True
            break
        else:
            print("Resultado: FALSO")
            print("Los nombres son diferentes.")
            print("Se continua con el siguiente producto.")

    print("\n========== RESULTADO ==========")

    if encontrado:
        print("Producto encontrado:", producto)
        print("Posicion comenzando desde 1:", i + 1)
    else:
        print("El producto no se encuentra en la lista.")

    print("Comparaciones realizadas:", comparaciones)
    print("Fin de la resolucion paso a paso.")


def principal():
    datos_ejemplo = ["Teclado", "Mouse", "Monitor", "Audifonos", "Bocinas"]
    objetivo_ejemplo = "Monitor"

    while True:
        print("\n========== BUSQUEDA SECUENCIAL DE PRODUCTOS ==========")
        print("1. Resolver ejemplo")
        print("2. Resolver mi propio ejercicio")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            buscar(datos_ejemplo, objetivo_ejemplo)

        elif opcion == "2":
            datos = [
                x.strip()
                for x in input("Ingresa los productos separados por comas: ").split(",")
                if x.strip()
            ]

            if not datos:
                print("Debes ingresar al menos un producto.")
                continue

            objetivo = input("Producto que deseas buscar: ").strip()

            if objetivo:
                buscar(datos, objetivo)
            else:
                print("Debes escribir el producto que deseas buscar.")

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    principal()
