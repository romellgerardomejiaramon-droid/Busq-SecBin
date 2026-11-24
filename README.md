# Busq-SecBin

# Sistema de Métodos de Búsqueda en Python

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un programa en Python que permite ejecutar tres algoritmos de búsqueda: búsqueda secuencial, búsqueda binaria y búsqueda hash. El programa cuenta con una interfaz gráfica desarrollada mediante Tkinter, en la que el usuario puede seleccionar el método que desea utilizar, resolver ejemplos predeterminados o introducir sus propios datos.

El sistema no solamente muestra el resultado de la búsqueda, sino que también presenta el procedimiento paso a paso durante la ejecución. De esta manera, es posible observar cómo trabaja cada algoritmo, qué comparaciones realiza, cómo toma sus decisiones y en qué momento encuentra el elemento solicitado.

Adicionalmente, cada procedimiento se muestra en la interfaz gráfica y en la terminal de Python, permitiendo visualizar y comprender el funcionamiento de los algoritmos desde ambos medios.

---

## Objetivo

Desarrollar un programa con menú que permita ejecutar los tres métodos de búsqueda estudiados: secuencial, binaria y hash, mediante una interfaz gráfica en Python.

El programa busca facilitar la comprensión de cada algoritmo, mostrando sus procedimientos, comparaciones, resultados y las operaciones que realiza durante la búsqueda de un elemento.

---

## Tecnologías utilizadas

- **Python:** lenguaje de programación utilizado para desarrollar la lógica de los algoritmos y el funcionamiento general del sistema.
- **Tkinter:** biblioteca utilizada para construir la interfaz gráfica, los botones, las ventanas, los campos de entrada y el panel de resultados.
- **Terminal:** medio adicional donde se imprime el procedimiento paso a paso de cada método ejecutado.

---

## Requisitos para ejecutar el programa

- Tener Python instalado.
- Contar con un editor de código, como Visual Studio Code.
- Disponer de Tkinter, que generalmente se incluye en las instalaciones estándar de Python para Windows.

No se requiere instalar librerías externas adicionales para ejecutar el programa.

---

# Funcionamiento externo del programa

## 1. Inicio del programa

Al ejecutar el archivo de Python, se abre una ventana gráfica que contiene el título del sistema y el menú principal. Desde esta pantalla se puede seleccionar alguno de los tres métodos de búsqueda disponibles o salir del programa.

El sistema está diseñado para que el usuario pueda recorrer las diferentes opciones sin necesidad de escribir comandos directamente en la interfaz, ya que la mayoría de las operaciones se realizan mediante botones.

## 2. Menú principal

El menú principal presenta cuatro opciones:

### 1. Búsqueda Secuencial

Permite acceder al menú del método secuencial, donde se puede ejecutar un ejemplo predeterminado o ingresar un ejercicio propio.

### 2. Búsqueda Binaria

Permite acceder al método de búsqueda binaria. Este algoritmo ordena automáticamente los números ingresados antes de iniciar el procedimiento.

### 3. Búsqueda Hash

Permite ejecutar el método hash, mediante el cual los elementos son almacenados en una tabla utilizando una función que calcula su posición.

### 4. Salir del programa

Permite cerrar la aplicación. Antes de cerrarla, se presenta una confirmación para evitar que el programa termine accidentalmente.

---

## 3. Menú de cada método

Después de seleccionar un método en el menú principal, se muestra una pantalla con las siguientes opciones:

- **Resolver ejemplo:** ejecuta un ejercicio con datos previamente definidos dentro del programa.
- **Resolver ejercicio propio:** permite introducir los datos y el elemento que se desea buscar.
- **Regresar al menú principal:** permite volver a la pantalla inicial sin ejecutar una búsqueda.
- **Salir del programa:** cierra la aplicación mediante una confirmación.

Esta estructura permite utilizar cualquiera de los tres métodos sin tener que reiniciar el programa cada vez que se quiera realizar otra búsqueda.

---

## 4. Resolver ejemplo

Al seleccionar la opción de resolver ejemplo, el programa utiliza una lista y un valor de búsqueda previamente establecidos para el método seleccionado.

Los ejemplos incluidos son:

| Método | Datos | Elemento buscado |
|---|---|---|
| Secuencial | 25, 10, 45, 30, 60, 15 | 30 |
| Binaria | 45, 10, 30, 20, 50, 40, 60 | 40 |
| Hash | 15, 22, 8, 29, 36, 43, 50, 22 | 36 |

Estos ejemplos permiten observar la ejecución de cada algoritmo sin necesidad de introducir los datos manualmente.

---

## 5. Resolver ejercicio propio

Esta opción permite que el usuario introduzca una lista de elementos separados por comas y posteriormente escriba el valor que desea buscar.

El programa recibe los datos mediante campos de texto, valida que no estén vacíos y, dependiendo del método seleccionado, procesa la información para ejecutar el algoritmo.

En la búsqueda binaria, los datos deben ser números enteros, ya que el algoritmo necesita comparar valores numéricos para determinar qué mitad de la lista descartar.

En la búsqueda secuencial y hash, los datos pueden introducirse como texto o números representados mediante texto.

### Ejemplo de entrada

**Datos:**

12, 45, 8, 30, 17, 45, 60

**Elemento buscado:**

30

Al presionar el botón de resolver ejercicio, se inicia el procedimiento del algoritmo correspondiente.

---

## 6. Visualización de la resolución

Cuando se ejecuta un método, se abre una pantalla de resultados que muestra el procedimiento de la búsqueda.

En esta pantalla se pueden observar:

- Los datos utilizados.
- El elemento que se busca.
- Las operaciones realizadas.
- Las comparaciones efectuadas.
- Los cambios que realiza el algoritmo.
- El resultado final.
- El número de comparaciones.

La pantalla cuenta con barras de desplazamiento vertical y horizontal, permitiendo visualizar el procedimiento completo aunque el resultado ocupe más espacio del disponible.

---

## 7. Procedimiento en la terminal

Además de mostrar los resultados en la interfaz gráfica, el programa imprime el procedimiento en la terminal de Python.

Al ejecutar una búsqueda, la terminal muestra el método seleccionado, los datos utilizados, el elemento buscado y las operaciones que realiza el algoritmo durante su ejecución.

Esto permite observar el funcionamiento del programa de manera simultánea en la interfaz gráfica y en la consola.

La terminal presenta información organizada mediante separadores y pasos, facilitando la lectura de las comparaciones, las decisiones y los resultados.

---

## 8. Regresar al menú principal o salir

Después de terminar la resolución de un ejercicio, el programa presenta dos opciones:

- **Regresar al menú principal:** permite seleccionar nuevamente cualquiera de los tres métodos de búsqueda.
- **Salir del programa:** permite cerrar la aplicación.

Esto facilita realizar diferentes ejercicios consecutivamente dentro de una sola ejecución del programa.

---

# Funcionamiento interno del programa

## 1. Clase `SistemaBusquedas`

La clase `SistemaBusquedas` contiene la estructura principal del programa. Dentro de ella se encuentran los métodos que controlan la interfaz gráfica, los menús, la entrada de datos, la ejecución de los algoritmos, la presentación de los resultados y la navegación.

La clase permite organizar el sistema en diferentes funciones, evitando concentrar todo el funcionamiento en un único bloque de código.

### Método `__init__(self, ventana)`

Es el constructor de la clase. Se ejecuta cuando se crea una instancia de `SistemaBusquedas`.

Sus principales funciones son:

- Recibir la ventana principal de Tkinter.
- Establecer el título de la aplicación.
- Definir el tamaño inicial de la ventana.
- Establecer el tamaño mínimo.
- Intentar maximizar la ventana.
- Definir los colores utilizados en la interfaz.
- Crear el contenedor principal.
- Inicializar el menú principal.

Este método permite preparar todos los elementos necesarios para que el sistema pueda comenzar a funcionar.

---

## 2. Método `limpiar()`

Este método elimina los elementos gráficos que se encuentran dentro del contenedor principal.

Recorre los widgets existentes mediante `winfo_children()` y los elimina utilizando `destroy()`.

Su función es permitir que el programa cambie entre los diferentes menús y pantallas sin crear ventanas adicionales innecesarias ni mantener elementos de pantallas anteriores.

Se utiliza cuando se cambia de menú, se abre un ejercicio propio o se muestran los resultados de una búsqueda.

---

## 3. Método `encabezado(titulo, subtitulo)`

Este método crea la sección superior de las diferentes pantallas del programa.

Recibe dos parámetros:

- `titulo`: texto principal que identifica la pantalla.
- `subtitulo`: texto complementario que explica la sección.

Utiliza un `Frame` para organizar los elementos y dos etiquetas `Label` para mostrar el título y el subtítulo.

Permite mantener una presentación visual uniforme en los menús y en la pantalla de resolución.

---

## 4. Método `boton(padre, texto, comando, color, ancho=30)`

Este método permite crear botones reutilizables dentro de la interfaz gráfica.

Recibe los siguientes parámetros:

- `padre`: contenedor donde se colocará el botón.
- `texto`: texto que se mostrará en el botón.
- `comando`: función que se ejecutará cuando se presione.
- `color`: color de fondo del botón.
- `ancho`: tamaño horizontal del botón.

Utiliza `tk.Button` para construir el botón y establece características como el tamaño de letra, el color, el cursor y el espacio interno.

Al reutilizar este método, se evita repetir la configuración de los botones en cada menú.

---

## 5. Método `menu_principal()`

Este método construye la pantalla inicial del programa.

Primero limpia el contenedor, posteriormente crea el encabezado y organiza los botones correspondientes a los tres algoritmos de búsqueda y la opción de salir.

Cada botón está relacionado con una función mediante `command`, lo que permite ejecutar una acción cuando el usuario selecciona una opción.

Las opciones del menú principal son:

- Búsqueda Secuencial.
- Búsqueda Binaria.
- Búsqueda Hash.
- Salir del programa.

Cuando se selecciona un método, se llama a `menu_metodo()` y se envía como parámetro el nombre del algoritmo que se desea utilizar.

---

## 6. Método `menu_metodo(metodo)`

Este método crea el menú correspondiente al algoritmo seleccionado.

Recibe el nombre del método mediante el parámetro `metodo`, lo almacena en `self.metodo_actual` y construye una pantalla con cuatro opciones.

### Resolver ejemplo

Ejecuta la función `resolver_ejemplo()`, que selecciona los datos predeterminados correspondientes al método actual.

### Resolver ejercicio propio

Ejecuta la función `resolver_usuario()`, donde el usuario puede introducir sus propios datos.

### Regresar al menú principal

Ejecuta `menu_principal()`, permitiendo volver a la pantalla inicial.

### Salir del programa

Ejecuta `salir()`, que solicita confirmación antes de cerrar la aplicación.

Este método permite mantener la navegación organizada y utilizar una estructura de menú para los tres algoritmos.

---

## 7. Método `resolver_ejemplo()`

Este método determina qué datos y qué valor se utilizarán dependiendo del algoritmo seleccionado.

Utiliza una estructura condicional `if`, `elif` y `else` para identificar el método actual.

### Ejemplo para búsqueda secuencial

Se utiliza la lista:

`["25", "10", "45", "30", "60", "15"]`

El elemento que se busca es `30`.

### Ejemplo para búsqueda binaria

Se utiliza la lista:

`[45, 10, 30, 20, 50, 40, 60]`

El elemento que se busca es `40`.

### Ejemplo para búsqueda hash

Se utiliza la lista:

`["15", "22", "8", "29", "36", "43", "50", "22"]`

El elemento que se busca es `36`.

Después de seleccionar los datos correspondientes, el método llama a `ejecutar(datos, buscar)`, que inicia el procedimiento y muestra los resultados.

---

## 8. Método `resolver_usuario()`

Este método permite ingresar un ejercicio personalizado.

Primero limpia la pantalla y crea una nueva interfaz con campos de entrada para los datos y el valor que se desea buscar.

### Entrada de datos

Se utiliza un campo `Entry` donde el usuario escribe una lista de elementos separados por comas.

### Entrada del elemento buscado

Se utiliza otro campo `Entry` para escribir el valor que se desea encontrar.

### Función interna `ejecutar()`

Dentro de `resolver_usuario()` se define una función llamada `ejecutar()`, que se activa cuando se presiona el botón Resolver ejercicio.

Esta función realiza las siguientes operaciones:

1. Obtiene los datos ingresados.
2. Obtiene el valor buscado.
3. Comprueba que ambos campos contengan información.
4. Divide los datos utilizando las comas.
5. Elimina espacios innecesarios.
6. Si se seleccionó búsqueda binaria, convierte los datos y el valor buscado a números enteros.
7. Si la conversión no es válida, muestra un mensaje de error.
8. Si los datos son correctos, llama a `ejecutar(datos, buscar)`.

Esta función permite validar los datos antes de comenzar el procedimiento del algoritmo.

---

## 9. Método `pantalla_resultados()`

Este método construye la pantalla donde se presenta el procedimiento de la búsqueda.

Primero elimina los elementos anteriores y crea un encabezado con el nombre del método.

Posteriormente, crea un panel que contiene un widget `Text`, donde se mostrarán los pasos de la resolución.

### Widget `Text`

Es el área donde se imprime el procedimiento. Permite mostrar varias líneas de información y utilizar desplazamiento para consultar los resultados.

### Barra de desplazamiento vertical

Permite recorrer el contenido de arriba hacia abajo cuando la resolución ocupa más espacio del disponible.

### Barra de desplazamiento horizontal

Permite desplazarse horizontalmente cuando las líneas de texto son demasiado largas.

Este método configura las barras de desplazamiento mediante `Scrollbar` y las relaciona con el widget `Text`.

Finalmente, almacena el área de texto en `self.texto_resultado`, permitiendo que otros métodos puedan escribir directamente en ella.

---

## 10. Método `registrar(mensaje="")`

Este método se encarga de mostrar información durante la ejecución del programa.

Recibe un mensaje como parámetro y lo presenta en dos medios:

- En la interfaz gráfica, mediante `self.texto_resultado.insert()`.
- En la terminal, mediante `print()`.

También utiliza `see("end")` para desplazar automáticamente el panel gráfico hacia la última línea que se ha escrito.

Este método es importante porque permite que los tres algoritmos presenten sus procedimientos de manera uniforme, sin tener que repetir las instrucciones de impresión en cada parte del programa.

---

## 11. Método `ejecutar(datos, buscar)`

Este método es el encargado de iniciar la resolución del algoritmo seleccionado.

Recibe dos parámetros:

- `datos`: lista de elementos que se utilizarán en la búsqueda.
- `buscar`: elemento que se desea encontrar.

### Funcionamiento

1. Crea la pantalla de resultados mediante `pantalla_resultados()`.
2. Habilita el widget de texto para escribir.
3. Imprime en la terminal los datos y el elemento buscado.
4. Registra los datos iniciales en la interfaz gráfica.
5. Identifica el algoritmo mediante una estructura condicional.
6. Ejecuta el método `secuencial()`, `binaria()` o `hash()`.
7. Registra el final del procedimiento.
8. Bloquea nuevamente el widget de texto.
9. Llama a `navegacion_final()` para presentar las opciones de regresar o salir.

Este método funciona como punto de conexión entre la interfaz gráfica y los algoritmos de búsqueda.

---

# Métodos de búsqueda

## 12. Método `secuencial(datos, buscar)`

La búsqueda secuencial es un algoritmo que permite encontrar un elemento recorriendo una lista desde el inicio hasta encontrar el valor buscado o hasta que se hayan revisado todos los elementos.

Este método no necesita que los datos estén ordenados previamente.

### Variables utilizadas

- `comparaciones`: cuenta el número de comparaciones realizadas.
- `posicion`: almacena la posición donde se encuentra el elemento. Inicialmente utiliza `-1` para indicar que no se ha encontrado.
- `i`: representa el índice del elemento que se está revisando.
- `elemento`: almacena el dato que se está comparando.

### Funcionamiento interno

1. Inicializa las comparaciones en cero y la posición en `-1`.
2. Recorre la lista mediante un ciclo `for`.
3. Obtiene el elemento correspondiente a la posición actual.
4. Incrementa el contador de comparaciones.
5. Muestra la posición, el elemento actual y el valor buscado.
6. Compara ambos valores.
7. Si coinciden, guarda la posición, muestra que encontró el elemento y detiene el ciclo mediante `break`.
8. Si no coinciden, continúa con el siguiente elemento.
9. Al terminar, muestra el resultado y las comparaciones realizadas.

En este programa, la comparación de los elementos se realiza convirtiéndolos a texto y utilizando `lower()` para permitir que las coincidencias de texto no dependan de las mayúsculas o minúsculas.

### Ejemplo de funcionamiento

Datos:

`["25", "10", "45", "30", "60", "15"]`

Elemento buscado:

`30`

El procedimiento comienza en la posición cero.

| Comparación | Posición | Elemento | Resultado |
|---|---:|---:|---|
| 1 | 0 | 25 | No coincide |
| 2 | 1 | 10 | No coincide |
| 3 | 2 | 45 | No coincide |
| 4 | 3 | 30 | Encontrado |

El algoritmo se detiene cuando encuentra el valor `30`, por lo que no revisa los elementos restantes.

### Resultado

El elemento se encuentra en la posición 3 y se realizaron cuatro comparaciones.

Las posiciones comienzan en cero, como sucede con los índices de las listas en Python.

### ¿Para qué sirve?

Este método sirve para localizar elementos en listas pequeñas, listas desordenadas o situaciones donde no es necesario realizar un ordenamiento previo.

Su principal ventaja es la sencillez de implementación. Sin embargo, si la lista es muy grande y el elemento se encuentra al final o no existe, puede necesitar revisar todos los elementos.

### Complejidad

- Mejor caso: O(1).
- Caso promedio: O(n).
- Peor caso: O(n).

---

## 13. Método `binaria(datos, buscar)`

La búsqueda binaria es un algoritmo que permite encontrar un elemento en una lista ordenada. Su funcionamiento consiste en comparar el elemento buscado con el valor ubicado en el centro de la lista y, dependiendo del resultado, descartar la mitad que no necesita revisar.

En este programa, la lista se ordena automáticamente antes de comenzar la búsqueda.

### Variables utilizadas

- `comparaciones`: cuenta las comparaciones realizadas.
- `posicion`: almacena la posición donde se encuentra el elemento.
- `izquierda`: representa el límite izquierdo del intervalo de búsqueda.
- `derecha`: representa el límite derecho del intervalo de búsqueda.
- `centro`: representa la posición central calculada.
- `elemento`: almacena el valor ubicado en el centro.

### Funcionamiento interno

#### Paso 1. Ordenamiento

Se utiliza `sorted(datos)` para ordenar la lista de menor a mayor.

Este paso es necesario porque la búsqueda binaria utiliza el orden de los elementos para determinar qué mitad descartar.

#### Paso 2. Definir los límites

Se establece el límite izquierdo en cero y el derecho en la última posición de la lista.

#### Paso 3. Calcular el centro

Se utiliza la expresión:

`centro = (izquierda + derecha) // 2`

El operador `//` permite obtener un número entero, que corresponde al índice central del intervalo.

#### Paso 4. Comparar el elemento central

Se compara el valor central con el elemento buscado.

- Si son iguales, se encontró el elemento.
- Si el valor central es menor que el buscado, se descarta la mitad izquierda y se actualiza el límite izquierdo.
- Si el valor central es mayor que el buscado, se descarta la mitad derecha y se actualiza el límite derecho.

#### Paso 5. Repetir

El proceso se repite mientras `izquierda <= derecha`.

Si el elemento se encuentra, se detiene la búsqueda. Si los límites se cruzan, significa que el elemento no está presente.

### Ejemplo de funcionamiento

Datos originales:

`[45, 10, 30, 20, 50, 40, 60]`

Elemento buscado:

`40`

#### Paso 1. Ordenar

La lista queda:

`[10, 20, 30, 40, 45, 50, 60]`

#### Paso 2. Primera comparación

- Izquierda: 0.
- Derecha: 6.
- Centro: 3.
- Valor central: 40.

El valor central coincide con el buscado.

#### Paso 3. Resultado

El elemento se encuentra en la posición 3 de la lista ordenada.

Se realiza una comparación.

### ¿Para qué sirve?

Este método sirve para buscar elementos en listas ordenadas de manera eficiente.

Su principal ventaja es que reduce el intervalo de búsqueda aproximadamente a la mitad en cada iteración, lo que permite localizar elementos rápidamente cuando se trabaja con grandes cantidades de datos ordenados.

### Complejidad

- Mejor caso: O(1).
- Caso promedio: O(log n).
- Peor caso: O(log n) para la búsqueda.

El ordenamiento previo también tiene un costo. En Python, `sorted()` tiene una complejidad de O(n log n) en el caso general.

---

## 14. Método `hash(datos, buscar)`

La búsqueda hash utiliza una función para calcular la posición donde se almacena cada elemento dentro de una tabla.

En este programa se utiliza una tabla de tamaño siete y un mecanismo de encadenamiento mediante cubetas, donde cada posición puede contener una lista de elementos.

El encadenamiento permite almacenar varios elementos en una misma posición cuando se producen colisiones.

### Variables utilizadas

- `tamaño`: define la cantidad de posiciones de la tabla hash, establecida en siete.
- `tabla`: representa la tabla hash, formada por listas que funcionan como cubetas.
- `comparaciones`: cuenta las comparaciones realizadas durante la búsqueda.
- `posicion_encontrada`: almacena la posición del elemento dentro de la cubeta.
- `posicion_hash`: representa la posición calculada mediante la función hash.

### Función interna `normalizar(valor)`

Esta función convierte el valor recibido en texto, elimina espacios al inicio y al final y transforma las letras a minúsculas.

Se utiliza para que la comparación de texto no dependa de las mayúsculas o minúsculas.

### Función interna `funcion_hash(valor)`

Esta función calcula la posición donde se debe almacenar o buscar un elemento.

Primero normaliza el valor recibido.

Si el elemento está formado únicamente por dígitos, utiliza el valor numérico y calcula el residuo de su división entre siete.

Si el elemento es texto, suma los códigos de sus caracteres mediante `ord()` y calcula el residuo de esa suma entre siete.

De esta manera, se obtiene una posición entre cero y seis.

### Funcionamiento interno

#### Paso 1. Crear la tabla

Se crea una lista de siete posiciones, donde cada posición contiene una lista vacía.

Estas listas funcionan como cubetas y permiten almacenar elementos cuando existen colisiones.

#### Paso 2. Insertar los elementos

El programa recorre todos los elementos de la lista original.

Para cada elemento:

1. Calcula su posición mediante la función hash.
2. Comprueba si la cubeta está vacía.
3. Si está vacía, agrega el elemento.
4. Si ya contiene elementos, informa que existe una colisión.
5. Agrega el nuevo elemento a la misma cubeta.

El encadenamiento permite conservar los elementos que generan la misma posición.

#### Paso 3. Mostrar la tabla

Se recorre la tabla hash y se muestra el contenido de cada posición.

Esto permite observar cómo se distribuyeron los elementos y en qué cubetas se produjeron colisiones.

#### Paso 4. Calcular la posición del elemento buscado

Se utiliza la misma función hash para calcular la posición correspondiente al elemento que se desea encontrar.

Esto permite acceder directamente a la cubeta donde debería encontrarse el elemento.

#### Paso 5. Buscar dentro de la cubeta

El programa recorre únicamente los elementos de la cubeta correspondiente.

Cada elemento se compara con el valor buscado.

Si coincide, se registra la posición dentro de la cubeta y se detiene la búsqueda.

Si no coincide, continúa revisando los elementos restantes de esa cubeta.

#### Paso 6. Mostrar el resultado

Se informa si el elemento fue encontrado, la posición hash, la posición dentro de la cubeta y el número de comparaciones realizadas.

### Ejemplo de funcionamiento

Datos:

`["15", "22", "8", "29", "36", "43", "50", "22"]`

Elemento buscado:

`36`

Tamaño de la tabla:

`7`

Para el elemento `36`, se calcula:

`36 % 7 = 1`

Por lo tanto, el elemento se almacena en la posición 1 de la tabla.

En este ejemplo, los elementos numéricos se distribuyen mediante el residuo de su división entre siete.

### Ejemplo de tabla hash

| Posición | Elementos |
|---|---|
| 0 | [50] |
| 1 | [22, 36, 43, 22] |
| 2 | [15, 29] |
| 3 | [] |
| 4 | [] |
| 5 | [] |
| 6 | [8] |

El elemento `36` se encuentra en la cubeta 1. El programa revisa los elementos de esa cubeta hasta encontrar la coincidencia.

### ¿Para qué sirve?

Este método sirve para localizar elementos mediante posiciones calculadas a partir de una función hash.

Es utilizado en estructuras de datos donde se busca facilitar el acceso a la información, como tablas hash, diccionarios, sistemas de almacenamiento de claves y estructuras de consulta.

Su principal ventaja es que, cuando los elementos están bien distribuidos y las colisiones son pocas, la búsqueda puede realizarse de manera muy rápida.

### Complejidad

- Caso promedio: O(1) bajo una distribución favorable y un factor de carga controlado.
- Peor caso: O(n), cuando muchos elementos se concentran en una misma cubeta.

---

# Funcionamiento interno de la navegación

## 15. Método `navegacion_final()`

Este método crea los botones que aparecen después de terminar la resolución de un ejercicio.

Presenta dos opciones:

- Regresar al menú principal.
- Salir del programa.

El botón para regresar ejecuta `menu_principal()`, mientras que el botón para salir ejecuta `salir()`.

Permite continuar realizando ejercicios dentro del mismo programa sin necesidad de cerrarlo.

---

## 16. Método `salir()`

Este método permite cerrar la aplicación de manera controlada.

Utiliza `messagebox.askyesno()` para mostrar un cuadro de confirmación.

Si el usuario confirma la salida, se ejecuta `self.ventana.destroy()`, que cierra la ventana principal de Tkinter.

Si el usuario selecciona que no desea salir, la aplicación permanece abierta.

---

# Inicio de la aplicación

Al final del archivo se encuentran las instrucciones que permiten iniciar el sistema.

```python
ventana = tk.Tk()
app = SistemaBusquedas(ventana)
ventana.mainloop()
```

### `ventana = tk.Tk()`

Crea la ventana principal de la aplicación mediante Tkinter.

### `app = SistemaBusquedas(ventana)`

Crea una instancia de la clase `SistemaBusquedas`, ejecutando su constructor y preparando los elementos iniciales del sistema.

### `ventana.mainloop()`

Inicia el ciclo de eventos de Tkinter. Este ciclo mantiene la ventana abierta, permite detectar las acciones del usuario y ejecutar las funciones asociadas a los botones.

---

# Recorrido completo del programa

El funcionamiento general del sistema puede resumirse de la siguiente manera:

1. Se crea la ventana principal.
2. Se inicializa la clase `SistemaBusquedas`.
3. Se muestra el menú principal.
4. El usuario selecciona uno de los tres métodos.
5. Se muestra el menú correspondiente al método.
6. El usuario selecciona resolver ejemplo o ejercicio propio.
7. Se obtienen los datos y el valor buscado.
8. Se crea la pantalla de resultados.
9. Se ejecuta el algoritmo correspondiente.
10. Se muestran los pasos en Tkinter y en la terminal.
11. Se presenta el resultado final.
12. El usuario puede regresar al menú principal o salir.

---

# Cómo ejecutar el programa

## 1. Descargar o clonar el repositorio

Descarga el proyecto desde GitHub o clónalo utilizando Git.

## 2. Abrir el archivo

Abre el archivo `SistemaBusquedas.py` en Visual Studio Code.

## 3. Abrir la terminal

En Visual Studio Code, selecciona Terminal y posteriormente Nueva terminal.

## 4. Ejecutar el programa

Escribe el siguiente comando:

```bash
python SistemaBusquedas.py
```

Si tu instalación utiliza el comando `py`, también puedes ejecutar:

```bash
py SistemaBusquedas.py
```

## 5. Utilizar el sistema

Cuando se abra la ventana:

1. Selecciona el método de búsqueda.
2. Selecciona resolver ejemplo o ejercicio propio.
3. Observa la resolución en la interfaz gráfica.
4. Observa también el procedimiento en la terminal.
5. Regresa al menú principal para realizar otra búsqueda o selecciona salir.

---

# Conclusión

El desarrollo de este programa permitió integrar los métodos de búsqueda secuencial, binaria y hash en una sola aplicación, utilizando Python y Tkinter para crear una interfaz gráfica que facilita la ejecución y comprensión de los algoritmos. Cada método fue organizado mediante funciones independientes, lo que permite mantener una estructura clara y facilita la identificación de las operaciones que realiza cada uno.

La búsqueda secuencial permite observar cómo se revisan los elementos uno por uno; la búsqueda binaria demuestra la importancia del ordenamiento y la reducción de intervalos; y la búsqueda hash permite comprender cómo una función calcula posiciones dentro de una tabla y cómo se manejan las colisiones mediante cubetas.

Además, la presentación de los procedimientos en la interfaz gráfica y en la terminal permite visualizar las comparaciones, las decisiones y los resultados durante la ejecución, haciendo que el programa no se limite a encontrar un elemento, sino que también permita comprender cómo se realiza la búsqueda.

El programa cumple con el objetivo de integrar los tres métodos de búsqueda en un sistema con menú, ejemplos, ejercicios propios, resultados detallados y navegación entre las diferentes opciones.
