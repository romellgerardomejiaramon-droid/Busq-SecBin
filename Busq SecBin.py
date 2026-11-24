
import tkinter as tk
from tkinter import messagebox


class SistemaBusquedas:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Metodos de Busqueda")
        self.ventana.geometry("1200x800")
        self.ventana.minsize(950, 650)

        try:
            self.ventana.state("zoomed")
        except:
            pass

        self.fondo = "#F0F4F8"
        self.azul = "#1E3A5F"
        self.verde = "#198754"
        self.naranja = "#E67E22"
        self.rojo = "#C0392B"

        self.ventana.configure(bg=self.fondo)

        self.contenedor = tk.Frame(
            self.ventana,
            bg=self.fondo
        )
        self.contenedor.pack(fill="both", expand=True)

        self.metodo_actual = ""

        self.menu_principal()

    def limpiar(self):
        for widget in self.contenedor.winfo_children():
            widget.destroy()

    def encabezado(self, titulo, subtitulo):
        panel = tk.Frame(
            self.contenedor,
            bg=self.azul
        )
        panel.pack(fill="x")

        tk.Label(
            panel,
            text=titulo,
            font=("Arial", 22, "bold"),
            bg=self.azul,
            fg="white"
        ).pack(pady=(15, 5))

        tk.Label(
            panel,
            text=subtitulo,
            font=("Arial", 12),
            bg=self.azul,
            fg="white"
        ).pack(pady=(0, 15))

    def boton(self, padre, texto, comando, color, ancho=30):
        return tk.Button(
            padre,
            text=texto,
            command=comando,
            font=("Arial", 13, "bold"),
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=ancho,
            pady=10
        )

    def menu_principal(self):
        self.limpiar()

        self.encabezado(
            "SISTEMA DE METODOS DE BUSQUEDA",
            "Programa integrador de algoritmos de busqueda"
        )

        panel = tk.Frame(
            self.contenedor,
            bg=self.fondo
        )
        panel.pack(expand=True)

        tk.Label(
            panel,
            text="MENU PRINCIPAL",
            font=("Arial", 20, "bold"),
            fg=self.azul,
            bg=self.fondo
        ).pack(pady=25)

        self.boton(
            panel,
            "1. Busqueda Secuencial",
            lambda: self.menu_metodo("Secuencial"),
            self.verde,
            38
        ).pack(pady=12)

        self.boton(
            panel,
            "2. Busqueda Binaria",
            lambda: self.menu_metodo("Binaria"),
            "#2874A6",
            38
        ).pack(pady=12)

        self.boton(
            panel,
            "3. Busqueda Hash",
            lambda: self.menu_metodo("Hash"),
            self.naranja,
            38
        ).pack(pady=12)

        self.boton(
            panel,
            "4. Salir del programa",
            self.salir,
            self.rojo,
            38
        ).pack(pady=12)

    def menu_metodo(self, metodo):
        self.limpiar()
        self.metodo_actual = metodo

        self.encabezado(
            "METODO DE BUSQUEDA " + metodo.upper(),
            "Selecciona como deseas realizar la busqueda"
        )

        panel = tk.Frame(
            self.contenedor,
            bg=self.fondo
        )
        panel.pack(expand=True)

        tk.Label(
            panel,
            text="MENU DEL METODO",
            font=("Arial", 20, "bold"),
            fg=self.azul,
            bg=self.fondo
        ).pack(pady=25)

        self.boton(
            panel,
            "Resolver ejemplo",
            self.resolver_ejemplo,
            self.verde,
            38
        ).pack(pady=12)

        self.boton(
            panel,
            "Resolver ejercicio propio",
            self.resolver_usuario,
            "#2874A6",
            38
        ).pack(pady=12)

        self.boton(
            panel,
            "Regresar al menu principal",
            self.menu_principal,
            "#7F8C8D",
            38
        ).pack(pady=12)

        self.boton(
            panel,
            "Salir del programa",
            self.salir,
            self.rojo,
            38
        ).pack(pady=12)

    def resolver_ejemplo(self):

        if self.metodo_actual == "Secuencial":
            datos = ["25", "10", "45", "30", "60", "15"]
            buscar = "30"

        elif self.metodo_actual == "Binaria":
            datos = [45, 10, 30, 20, 50, 40, 60]
            buscar = 40

        else:
            datos = ["15", "22", "8", "29", "36", "43", "50", "22"]
            buscar = "36"

        self.ejecutar(datos, buscar)

    def resolver_usuario(self):
        self.limpiar()

        self.encabezado(
            "EJERCICIO PROPIO",
            "Escribe tus datos y el elemento que deseas buscar"
        )

        panel = tk.Frame(
            self.contenedor,
            bg=self.fondo
        )
        panel.pack(expand=True)

        tk.Label(
            panel,
            text="Ingresa los datos separados por comas:",
            font=("Arial", 14, "bold"),
            bg=self.fondo
        ).pack(pady=10)

        entrada_datos = tk.Entry(
            panel,
            width=65,
            font=("Arial", 14)
        )
        entrada_datos.pack(pady=10)

        tk.Label(
            panel,
            text="Elemento que deseas buscar:",
            font=("Arial", 14, "bold"),
            bg=self.fondo
        ).pack(pady=10)

        entrada_buscar = tk.Entry(
            panel,
            width=35,
            font=("Arial", 14)
        )
        entrada_buscar.pack(pady=10)

        def ejecutar():

            datos_texto = entrada_datos.get().strip()
            buscar_texto = entrada_buscar.get().strip()

            if not datos_texto or not buscar_texto:
                messagebox.showwarning(
                    "Datos incompletos",
                    "Debes ingresar los datos y el elemento a buscar."
                )
                return

            datos = [
                elemento.strip()
                for elemento in datos_texto.split(",")
                if elemento.strip()
            ]

            buscar = buscar_texto

            if self.metodo_actual == "Binaria":
                try:
                    datos = [int(x) for x in datos]
                    buscar = int(buscar)
                except ValueError:
                    messagebox.showerror(
                        "Error",
                        "La busqueda binaria solamente trabaja con numeros enteros."
                    )
                    return

            self.ejecutar(datos, buscar)

        self.boton(
            panel,
            "Resolver ejercicio",
            ejecutar,
            self.verde,
            30
        ).pack(pady=20)

        self.boton(
            panel,
            "Regresar al menu principal",
            self.menu_principal,
            "#7F8C8D",
            30
        ).pack(pady=10)

    def pantalla_resultados(self):
        self.limpiar()

        self.encabezado(
            "RESOLUCION PASO A PASO",
            "Metodo: " + self.metodo_actual
        )

        panel = tk.Frame(
            self.contenedor,
            bg=self.fondo
        )
        panel.pack(fill="both", expand=True, padx=15, pady=10)

        texto = tk.Text(
            panel,
            font=("Consolas", 12),
            bg="white",
            fg="#202020",
            wrap="none",
            padx=10,
            pady=10
        )

        scroll_vertical = tk.Scrollbar(
            panel,
            orient="vertical",
            command=texto.yview
        )

        scroll_horizontal = tk.Scrollbar(
            panel,
            orient="horizontal",
            command=texto.xview
        )

        texto.configure(
            yscrollcommand=scroll_vertical.set,
            xscrollcommand=scroll_horizontal.set
        )

        texto.pack(
            side="left",
            fill="both",
            expand=True
        )

        scroll_vertical.pack(
            side="right",
            fill="y"
        )

        scroll_horizontal.pack(
            side="bottom",
            fill="x"
        )

        self.texto_resultado = texto

    def registrar(self, mensaje=""):
        self.texto_resultado.insert(
            "end",
            mensaje + "\n"
        )

        self.texto_resultado.see("end")

        print(mensaje)

    def ejecutar(self, datos, buscar):

        self.pantalla_resultados()

        self.texto_resultado.configure(
            state="normal"
        )

        print("\n" + "=" * 65)
        print("RESOLUCION DEL METODO:", self.metodo_actual)
        print("Datos:", datos)
        print("Elemento buscado:", buscar)
        print("=" * 65)

        self.registrar("=" * 65)
        self.registrar("METODO: " + self.metodo_actual)
        self.registrar("DATOS: " + str(datos))
        self.registrar("ELEMENTO BUSCADO: " + str(buscar))
        self.registrar("=" * 65)
        self.registrar("")

        if self.metodo_actual == "Secuencial":
            self.secuencial(datos, buscar)

        elif self.metodo_actual == "Binaria":
            self.binaria(datos, buscar)

        elif self.metodo_actual == "Hash":
            self.hash(datos, buscar)

        self.registrar("")
        self.registrar("=" * 65)
        self.registrar("FIN DE LA RESOLUCION")
        self.registrar("=" * 65)

        self.texto_resultado.configure(
            state="disabled"
        )

        self.navegacion_final()

    # =====================================================
    # METODO DE BUSQUEDA SECUENCIAL
    # =====================================================

    def secuencial(self, datos, buscar):

        comparaciones = 0
        posicion = -1

        self.registrar("PASO 1: INICIO")
        self.registrar(
            "Se recorre la lista desde la primera posicion."
        )
        self.registrar(
            "Se compara cada elemento con el valor buscado."
        )
        self.registrar("")

        for i in range(len(datos)):

            elemento = datos[i]
            comparaciones += 1

            self.registrar("-" * 45)
            self.registrar("COMPARACION " + str(comparaciones))
            self.registrar(
                "Posicion actual: " + str(i)
            )
            self.registrar(
                "Elemento actual: " + str(elemento)
            )
            self.registrar(
                "Valor buscado: " + str(buscar)
            )
            self.registrar(
                "Se compara el elemento actual con el buscado."
            )

            if str(elemento).strip().lower() == str(buscar).strip().lower():

                posicion = i

                self.registrar(
                    "Resultado de la comparacion: COINCIDENCIA"
                )
                self.registrar(
                    "El elemento se encuentra en esta posicion."
                )
                self.registrar(
                    "Se detiene la busqueda."
                )
                break

            else:

                self.registrar(
                    "Resultado: NO COINCIDE"
                )
                self.registrar(
                    "Se continua con el siguiente elemento."
                )

            self.registrar("")

        self.registrar("")
        self.registrar("PASO 2: RESULTADO FINAL")

        if posicion != -1:

            self.registrar(
                "Elemento encontrado: " + str(buscar)
            )
            self.registrar(
                "Posicion: " + str(posicion)
            )

        else:

            self.registrar(
                "El elemento no se encuentra en la lista."
            )

        self.registrar(
            "Total de comparaciones: " + str(comparaciones)
        )

        self.registrar("")
        self.registrar("PASO 3: EXPLICACION")

        self.registrar(
            "La busqueda secuencial revisa los elementos"
        )
        self.registrar(
            "uno por uno hasta encontrar el valor o terminar."
        )

        self.registrar(
            "No requiere ordenar los datos previamente."
        )

    # =====================================================
    # METODO DE BUSQUEDA BINARIA
    # =====================================================

    def binaria(self, datos, buscar):

        comparaciones = 0
        posicion = -1

        self.registrar("PASO 1: ORDENAMIENTO")
        self.registrar(
            "La busqueda binaria requiere una lista ordenada."
        )
        self.registrar(
            "Se ordenan los datos de menor a mayor."
        )

        datos = sorted(datos)

        self.registrar(
            "Lista ordenada: " + str(datos)
        )
        self.registrar("")

        self.registrar("PASO 2: DEFINIR LOS LIMITES")

        izquierda = 0
        derecha = len(datos) - 1

        self.registrar(
            "Limite izquierdo: " + str(izquierda)
        )
        self.registrar(
            "Limite derecho: " + str(derecha)
        )
        self.registrar(
            "Se calcula el centro de los limites."
        )
        self.registrar("")

        self.registrar("PASO 3: INICIO DE LA BUSQUEDA")

        while izquierda <= derecha:

            centro = (izquierda + derecha) // 2

            elemento = datos[centro]

            comparaciones += 1

            self.registrar("-" * 50)
            self.registrar(
                "ITERACION " + str(comparaciones)
            )
            self.registrar(
                "Limite izquierdo: " + str(izquierda)
            )
            self.registrar(
                "Limite derecho: " + str(derecha)
            )
            self.registrar(
                "Centro calculado: " + str(centro)
            )
            self.registrar(
                "Valor del centro: " + str(elemento)
            )
            self.registrar(
                "Valor buscado: " + str(buscar)
            )
            self.registrar("")

            if elemento == buscar:

                posicion = centro

                self.registrar(
                    "El valor central coincide con el buscado."
                )
                self.registrar(
                    "Se encontro el elemento."
                )
                self.registrar(
                    "La busqueda termina."
                )
                break

            elif elemento < buscar:

                self.registrar(
                    "El centro es menor que el valor buscado."
                )
                self.registrar(
                    "Se descarta la mitad izquierda."
                )
                self.registrar(
                    "Nuevo limite izquierdo: centro + 1"
                )

                izquierda = centro + 1

            else:

                self.registrar(
                    "El centro es mayor que el valor buscado."
                )
                self.registrar(
                    "Se descarta la mitad derecha."
                )
                self.registrar(
                    "Nuevo limite derecho: centro - 1"
                )

                derecha = centro - 1

            self.registrar(
                "Los limites se actualizan."
            )
            self.registrar("")

        self.registrar("")
        self.registrar("PASO 4: RESULTADO FINAL")

        if posicion != -1:

            self.registrar(
                "Elemento encontrado: " + str(buscar)
            )
            self.registrar(
                "Posicion en la lista ordenada: "
                + str(posicion)
            )

        else:

            self.registrar(
                "El elemento no se encuentra en la lista."
            )

        self.registrar(
            "Comparaciones realizadas: " + str(comparaciones)
        )

        self.registrar("")
        self.registrar("PASO 5: EXPLICACION")

        self.registrar(
            "La busqueda binaria compara el valor buscado"
        )
        self.registrar(
            "con el elemento ubicado en el centro."
        )
        self.registrar(
            "Dependiendo del resultado, descarta una mitad."
        )
        self.registrar(
            "Este proceso se repite hasta encontrar el valor"
        )
        self.registrar(
            "o hasta que los limites se crucen."
        )

    # =====================================================
    # METODO DE BUSQUEDA HASH
    # =====================================================

    def hash(self, datos, buscar):

        tamaño = 7
        tabla = [[] for _ in range(tamaño)]
        comparaciones = 0
        posicion_encontrada = -1

        def normalizar(valor):
            return str(valor).strip().lower()

        def funcion_hash(valor):

            clave = normalizar(valor)

            if clave.isdigit():

                return int(clave) % tamaño

            return sum(ord(c) for c in clave) % tamaño

        self.registrar("PASO 1: CREAR TABLA HASH")
        self.registrar(
            "Se crea una tabla de " + str(tamaño) + " posiciones."
        )
        self.registrar(
            "Se utilizaran cubetas para almacenar colisiones."
        )
        self.registrar(
            "Cada cubeta puede almacenar varios elementos."
        )
        self.registrar("")

        self.registrar("PASO 2: INSERTAR LOS DATOS")

        for elemento in datos:

            posicion = funcion_hash(elemento)

            self.registrar("-" * 50)
            self.registrar(
                "Elemento a insertar: " + str(elemento)
            )
            self.registrar(
                "Se calcula su posicion mediante la funcion hash."
            )
            self.registrar(
                "Posicion calculada: " + str(posicion)
            )

            if tabla[posicion]:

                self.registrar(
                    "COLISION: la cubeta ya contiene elementos."
                )
                self.registrar(
                    "Se agrega el elemento a la misma cubeta."
                )

            else:

                self.registrar(
                    "La cubeta se encuentra vacia."
                )
                self.registrar(
                    "Se agrega el elemento."
                )

            tabla[posicion].append(elemento)

            self.registrar(
                "Contenido actual de la cubeta: "
                + str(tabla[posicion])
            )
            self.registrar("")

        self.registrar("PASO 3: MOSTRAR TABLA HASH")

        for i in range(tamaño):

            self.registrar(
                str(i) + " -> " + str(tabla[i])
            )

        self.registrar("")
        self.registrar("PASO 4: BUSCAR EL ELEMENTO")

        posicion_hash = funcion_hash(buscar)

        self.registrar(
            "Elemento buscado: " + str(buscar)
        )
        self.registrar(
            "Se calcula la posicion hash del elemento."
        )
        self.registrar(
            "Posicion calculada: " + str(posicion_hash)
        )
        self.registrar(
            "Se revisa solamente la cubeta correspondiente."
        )
        self.registrar(
            "Cubeta: " + str(tabla[posicion_hash])
        )
        self.registrar("")

        for i, elemento in enumerate(tabla[posicion_hash]):

            comparaciones += 1

            self.registrar("-" * 45)
            self.registrar(
                "COMPARACION " + str(comparaciones)
            )
            self.registrar(
                "Elemento de la cubeta: " + str(elemento)
            )
            self.registrar(
                "Valor buscado: " + str(buscar)
            )

            if normalizar(elemento) == normalizar(buscar):

                posicion_encontrada = i

                self.registrar(
                    "COINCIDENCIA ENCONTRADA."
                )
                self.registrar(
                    "Se termina la busqueda."
                )
                break

            else:

                self.registrar(
                    "No coincide."
                )
                self.registrar(
                    "Se revisa el siguiente elemento de la cubeta."
                )

            self.registrar("")

        self.registrar("")
        self.registrar("PASO 5: RESULTADO FINAL")

        if posicion_encontrada != -1:

            self.registrar(
                "Elemento encontrado: " + str(buscar)
            )
            self.registrar(
                "Posicion hash: " + str(posicion_hash)
            )
            self.registrar(
                "Posicion dentro de la cubeta: "
                + str(posicion_encontrada)
            )

        else:

            self.registrar(
                "Elemento no encontrado en la tabla hash."
            )

        self.registrar(
            "Comparaciones realizadas: " + str(comparaciones)
        )

        self.registrar("")
        self.registrar("PASO 6: EXPLICACION")

        self.registrar(
            "Hash calcula una posicion mediante una funcion."
        )
        self.registrar(
            "Los elementos se almacenan en dicha posicion."
        )
        self.registrar(
            "Cuando ocurren colisiones, se utiliza una cubeta."
        )
        self.registrar(
            "La busqueda revisa los elementos de esa cubeta."
        )

    # =====================================================
    # NAVEGACION DESPUES DE RESOLVER
    # =====================================================

    def navegacion_final(self):

        panel = tk.Frame(
            self.contenedor,
            bg=self.fondo
        )
        panel.pack(fill="x", pady=10)

        self.boton(
            panel,
            "Regresar al menu principal",
            self.menu_principal,
            self.verde,
            30
        ).pack(side="left", expand=True, padx=10)

        self.boton(
            panel,
            "Salir del programa",
            self.salir,
            self.rojo,
            30
        ).pack(side="right", expand=True, padx=10)

    def salir(self):

        respuesta = messagebox.askyesno(
            "Salir del programa",
            "¿Deseas salir del programa?"
        )

        if respuesta:
            self.ventana.destroy()


ventana = tk.Tk()
app = SistemaBusquedas(ventana)
ventana.mainloop()
