# DESARROLLO
Su principal función consiste en leer los caracteres de entrada y elaborar como 
salida una secuencia de componentes léxicos que utiliza el analizador sintáctico 
para hacer el análisis. Esta interacción, suele aplicarse convirtiendo al analizador 
léxico en una subrutina o corrutina del analizador sintáctico. 

**FUNCIÓN SECUNDARIA**

Como el analizador léxico es .la parte del compilador que lee el texto fuente. 
También puede realizar ciertas funciones secundarias en la interfaz del usuario, 
como eliminar del programa fuente comentarios y espacios en blanco en forma de 
caracteres de espacio en blanco, caracteres TAB y de línea nueva. Otra función es 
relacionar os mensajes de error del compilador con el programa fuente. 
En algunos compiladores, el analizador léxico se encarga de hacer una copia del 
programa fuente en el que están marcados los mensajes de error. Si el lenguaje 
fuente es la base de algunas funciones de pre procesamiento de macros, entonces 
esas funciones del preprocesador también se pueden aplicar al hacer el análisis 
léxico. 

**FUENTE:** `#0969DA` 

http://cidecame.uaeh.edu.mx/lcc/mapa/PROYECTO/libro32/21_funcin_del_analizador_lxico.html 

El analizador léxico. Se encarga de buscar los componentes léxicos o palabras que 
componen el programa fuente, según unas reglas o patrones. La entrada del 
analizador léxico podemos definirla como una secuencia de caracteres.

 **CARACTERISTICAS**
 
 
El analizador léxico tiene que dividir la secuencia de caracteres en palabras con 
significado propio y después convertirlo a una secuencia de terminales desde el 
punto de vista del analizador sintáctico, ya que es su entrada. El analizador léxico 
reconoce las palabras en función de una gramática regular de manera que sus no 
terminales se convierten en los elementos de entrada de fases posteriores. 

**FUNCIÓN**

Su principal función consiste en leer los caracteres de entrada y elaborar como 
salida una secuencia de componentes léxicos que utiliza el analizador sintáctico 
para hacer el análisis. Esta interacción, suele aplicarse convirtiendo al analizador 
léxico en una subrutina o corrutina del analizador sintáctico 
 Reconocer los identificadores de usuario, números, palabras reservadas del 
lenguaje y tratarlos correctamente con respecto a la tabla de símbolos (solo 
en los casos que debe de tratar con la tabla de símbolos).
Llevar la cuenta del número de línea por la que va leyendo, por si se produce 
algún error, dar información sobre donde se ha producido. 
Puede hacer funciones de preprocesador. 

**FUENTE:** `#0969DA` 
http://materiacompliladores3110.blogspot.com/2017/02/analizador-lexico.html/ 

# CONCLUSIÓN 
Los analizadores léxicos son fundamentales en el desarrollo de compiladores y 
lenguajes de programación, ya que proporcionan la base para el análisis posterior 
del código fuente. Su eficiencia, capacidad de manejo de errores y su papel en la 
generación de tokens son aspectos críticos para el rendimiento general del sistema.

> [!TIP]
> :+1: ANALIZADOR OBJETOS

# DESARROLLO OBJETOS
Un analizador sintáctico, también conocido como parser, es una parte crucial de los 
compiladores e intérpretes en la ciencia de la computación. Su función principal es 
analizar la estructura gramatical de un lenguaje de programación (o cualquier otro 
tipo de lenguaje formal) para determinar si cumple con las reglas sintácticas 
definidas por el lenguaje. 
 
Aquí están algunas de las funciones principales de un analizador sintáctico: 
 
Análisis de la estructura gramatical: El analizador sintáctico toma el código fuente 
como entrada y lo divide en una estructura jerárquica que refleje la gramática del 
lenguaje. Esta estructura puede ser representada mediante árboles sintácticos o 
mediante otras estructuras de datos. 
 
Verificación de la sintaxis: El analizador sintáctico verifica si el código fuente se 
ajusta a las reglas sintácticas del lenguaje de programación en cuestión. Si 
encuentra un error sintáctico, generalmente produce un mensaje de error indicando 
dónde ocurrió el error y qué tipo de error es. 
 
Producción de un árbol sintáctico o una representación interna: A partir del código 
fuente, el analizador sintáctico puede construir un árbol sintáctico que represente la 
estructura jerárquica del código. Este árbol es útil para las etapas posteriores del 
proceso de compilación o interpretación. 
 
Preparación para la generación de código intermedio: En los compiladores, el 
analizador sintáctico es una etapa previa crucial antes de la generación de código 
intermedio. El árbol sintáctico o la representación interna generada por el analizador 
sintáctico sirve como entrada para la fase de generación de código. 
 
Optimización sintáctica: En algunos casos, el analizador sintáctico puede aplicar 
optimizaciones a la estructura del código fuente para mejorar su rendimiento o su 
legibilidad, aunque este tipo de optimizaciones son menos comunes y suelen ser 
realizadas en etapas posteriores del proceso de compilación. 

**FUENTE:** `#0969DA` 
http://cidecame.uaeh.edu.mx/lcc/mapa/PROYECTO/libro32/31_funcion_del_analizador_sintctico.html 

# CÓDIGO
![Captura de pantalla 2024-03-09 212334](https://github.com/TortaAhogada02/Traductores-de-lenguaje/assets/102304790/41d17cb0-37c2-494c-8202-528f8afacae4)

# RESULTADO
![image](https://github.com/TortaAhogada02/Traductores-de-lenguaje/assets/102304790/2725e581-c060-41de-a129-06780b4bb750)

# CONCLUSIÓN 
La función principal del analizador sintáctico es garantizar que el código fuente 
cumpla con las reglas sintácticas del lenguaje de programación y preparar una 
representación interna adecuada para las etapas posteriores del proceso de 
compilación o interpretación. Tuve un poco de problemas al realizar este programa 
ya que quise hacer interfaz, pero no he manejado ninguna, comencé a estudiar más 
sobre esto y me encantaría que en futuros programas emplearlos.
