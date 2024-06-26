# BIERNVENIDO A MI PROYECTO DE TRADUCTORES DE LENGUAJE
> [!NOTE]
> Este proyecto tendra algunos errores tanto como edición o en sus archivos para que se tenga cuidado

## PROPOSITO DEL PROYECTO
Un compilador es una herramienta fundamental en el desarrollo de software que tiene varios propósitos clave. Su principal función es traducir el código fuente escrito en un lenguaje de programación (lenguaje fuente) a otro (lenguaje de destino), como el lenguaje de máquina, que puede ser ejecutado directamente por la computadora. 
Además, los compiladores pueden realizar varias tareas adicionales que mejoran la eficiencia y la velocidad del programa ejecutable. Estas pueden incluir la eliminación de código redundante, la reorganización de instrucciones para mejorar el acceso a la memoria, la simplificación de expresiones matemáticas, y otras técnicas de optimización.
![image](https://github.com/TortaAhogada02/Traductores-de-lenguaje/assets/102304790/7808a8e6-9d93-4b20-9e3a-3087a8defec6)

## REQUERIMIENTOS
* **Computadora**
![image](https://github.com/TortaAhogada02/Traductores-de-lenguaje/assets/102304790/146c70d6-4028-40c2-a7ce-859d83170194)

* **Python y sus extensiones**
![image](https://github.com/TortaAhogada02/Traductores-de-lenguaje/assets/102304790/12dc9848-7a48-4c2e-ac61-af7281024d52)

* **Ensamblador**
  
![image](https://github.com/TortaAhogada02/Traductores-de-lenguaje/assets/102304790/1519cec1-7183-4a06-b59d-c066f7ed0ea4)

## AUTOR
:cowboy_hat_face: **Omar Alejandro Quiroz Trujillo** 
`Foto especial por este 30 de abril`
![image](https://github.com/TortaAhogada02/Traductores-de-lenguaje/assets/102304790/9a6da839-f36a-46d0-a626-677e6d561ff6)

## ETAPAS
### [Analizador lexico](https://github.com/TortaAhogada02/Traductores-de-lenguaje/tree/ANALIZADOR-LEXICO).
El analizador léxico es la primera fase de un compilador y tiene las siguientes funciones principales:

1. Leer los caracteres del programa fuente de entrada, carácter por carácter, y agruparlos en unidades con significado llamadas componentes léxicos o tokens. Estos tokens son la entrada para la siguiente etapa del compilador, el analizador sintáctico.

2. Eliminar elementos irrelevantes del código fuente, como espacios en blanco, tabuladores y comentarios.

3. Identificar y clasificar los diferentes tipos de componentes léxicos, como palabras reservadas, identificadores, operadores, constantes numéricas, etc.

4. Mantener un registro del número de línea y columna donde se encontró cada componente léxico, para facilitar la generación de mensajes de error.

5. Realizar funciones de preprocesamiento, como la expansión de macros, si el lenguaje de programación lo requiere.

### [Analizador sintactico](https://github.com/TortaAhogada02/Traductores-de-lenguaje/tree/main/MINI%20ANALIZADOR%20SINTACTICO)

El analizador sintáctico es la fase del compilador que se encarga de verificar que la secuencia de tokens de entrada cumple con las reglas gramaticales especificadas para el lenguaje de programación. Sus principales funciones son:

1. Recibir los componentes léxicos (tokens) y producir como salida una representación del árbol sintáctico que reconoce la entrada de acuerdo a la gramática.
2. Interactuar con la Tabla de Símbolos, que mantiene todos los símbolos presentes en la entrada.
3. Verificar que los tipos de datos están asignados correctamente para evitar errores semánticos.
4. Generar código intermedio que permita la ejecución o interpretación de la entrada.
5. Informar de los errores sintácticos encontrados en la entrada.

### [GRAMATICA](https://github.com/TortaAhogada02/Traductores-de-lenguaje/tree/ULTIMA-PARTE/GRAMATICA%20COMPILADOR).
Una gramática formal es fundamental para el funcionamiento de un compilador, ya que define la estructura y sintaxis válida del lenguaje de programación que el compilador debe procesar. Aquí te explico cómo funciona una gramática en un compilador:
Definición de la sintaxis del lenguaje
La gramática define las reglas que especifican cómo deben estar estructurados los programas válidos en el lenguaje. Estas reglas incluyen la forma en que se deben escribir las declaraciones, expresiones, sentencias, etc.
Y Análisis sintáctico del compilador utiliza la gramática para analizar el código fuente del programa y verificar si cumple con las reglas sintácticas definidas. Esto se conoce como análisis sintáctico o parsing.

### [ARBOL](https://github.com/TortaAhogada02/Traductores-de-lenguaje/tree/ULTIMA-PARTE/Arbol)
En el proceso de análisis sintáctico, un compilador utiliza las reglas gramaticales definidas en la gramática formal del lenguaje para construir un árbol de derivación sintáctica que representa la estructura jerárquica del programa. Cada nodo del árbol corresponde a un símbolo no terminal o terminal de la gramática, y las aristas representan las reglas de producción que se aplican para derivar la estructura del programa.
Los árboles de derivación sintáctica son esenciales para identificar la estructura sintáctica correcta del código fuente y para detectar posibles errores o ambigüedades en la sintaxis. Además, estos árboles sirven como entrada para las fases posteriores del compilador, como el análisis semántico y la generación de código intermedio.

### [ETAPA FINAL](https://github.com/TortaAhogada02/Traductores-de-lenguaje/tree/ULTIMA-PARTE/etapa%20final)
Un compilador es una herramienta fundamental en el desarrollo de software que desempeña varias funciones clave en el proceso de transformar el código fuente de un programa en un formato ejecutable.

* **Traducción de código fuente**
Un compilador traduce el código fuente escrito en un lenguaje de programación de alto nivel a un código objeto o ejecutable que puede ser entendido y ejecutado por la computadora.

* **Detección de errores**
Durante el proceso de compilación, se realizan verificaciones sintácticas y semánticas para detectar errores en el código fuente, como errores de sintaxis, tipos de datos incorrectos o referencias a variables no declaradas.

* **Optimización de código**
Los compiladores realizan optimizaciones en el código generado para mejorar su eficiencia en términos de tiempo de ejecución, uso de memoria y rendimiento general del programa.

* **Portabilidad**
Los compiladores permiten que un programa escrito en un lenguaje de alto nivel pueda ejecutarse en diferentes plataformas y arquitecturas de hardware, ya que generan código objeto específico para la plataforma de destino.

* **Abstracción**
Los compiladores permiten a los programadores trabajar a un nivel de abstracción más alto al escribir código en lenguajes de programación de alto nivel, lo que facilita el desarrollo de software complejo y reduce la complejidad de la programación a nivel de máquina.

* **Facilita el desarrollo de software**
Al convertir el código fuente en un formato ejecutable, los compiladores permiten a los programadores crear aplicaciones y sistemas de software completos que pueden ser distribuidos y utilizados por los usuarios finales.
