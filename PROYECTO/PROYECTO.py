# Importa el módulo de expresiones regulares
import re

# Función para realizar el análisis léxico de una cadena de entrada
def lexico(input_string):
    # Inicializa listas y diccionario para almacenar tokens y la tabla de símbolos
    tokens = []
    symbol_table = {}

    # Define patrones de expresiones regulares para diferentes tipos de tokens
    patterns = [
        (r'([a-zA-Z][a-zA-Z0-9]*)', 'ID'),       # Identificador
        (r'(\d+)', 'ENTERO'),                     # Entero
        (r'(\d+\.\d+)', 'REAL'),                  # Real
        (r'(\+|\-)', 'OP_ADICION'),               # Operador de adición
        (r'(\*|\/)', 'OP_MULTIPLICACION'),        # Operador de multiplicación
        (r'=', 'OP_ASIGNACION'),                  # Operador de asignación
        (r'(<|>|<=|>=|!=|==)', 'OP_RELACIONAL'), # Operador relacional
        (r'&&', 'OP_AND'),                        # Operador And
        (r'\|\|', 'OP_OR'),                       # Operador Or
        (r'!', 'OP_NOT'),                         # Operador Not
        (r'\(', 'PARENTESIS_ABIERTO'),            # Paréntesis abierto
        (r'\)', 'PARENTESIS_CERRADO'),            # Paréntesis cerrado
        (r'{', 'LLAVE_ABIERTA'),                  # Llave abierta
        (r'}', 'LLAVE_CERRADA'),                  # Llave cerrada
        (r';', 'PUNTO_COMA'),                     # Punto y coma
    ]

    # Itera sobre los patrones
    for pattern, token_type in patterns:
        # Compila el patrón de expresión regular
        regex = re.compile(pattern)
        # Busca coincidencias en la cadena de entrada
        match = regex.match(input_string)

        # Mientras haya coincidencias
        while match:
            # Obtiene el valor coincidente (lexema)
            value = match.group()
            # Agrega el token a la lista de tokens
            tokens.append((token_type, value))
            # Actualiza la tabla de símbolos con el símbolo y su tipo
            symbol_table[value] = token_type
            # Actualiza la cadena de entrada eliminando el lexema y espacios en blanco iniciales
            input_string = input_string[len(value):].lstrip()
            # Busca la siguiente coincidencia en la cadena actualizada
            match = regex.match(input_string)

    # Devuelve la lista de tokens y la tabla de símbolos
    return tokens, symbol_table

# Función para generar y escribir la tabla de símbolos en un archivo de salida
def generar_tabla_simbolos(symbol_table, output_file):
    with open(output_file, 'w') as file:
        # Escribe la cabecera del archivo
        file.write("Símbolo\t\tTipo\n")
        file.write("---------------------\n")
        # Itera sobre la tabla de símbolos y escribe cada símbolo y su tipo
        for symbol, symbol_type in symbol_table.items():
            file.write(f"{symbol}\t\t{symbol_type}\n")

# Bloque principal del programa
if __name__ == "__main__":
    # Solicita al usuario ingresar una cadena para ser analizada
    input_string = input("Ingrese la cadena a analizar: ")
    
    # Llama a la función lexico para realizar el análisis léxico
    tokens, symbol_table = lexico(input_string)

    # Imprime los tokens generados
    print("\nTokens:", tokens)
    
    # Imprime la tabla de símbolos generada
    print("\nTabla de Símbolos:")
    for symbol, symbol_type in symbol_table.items():
        print(f"{symbol}\t\t{symbol_type}")

    # Solicita al usuario ingresar el nombre del archivo de salida para la tabla de símbolos
    output_file = input("Ingrese el nombre del archivo de salida para la tabla de símbolos: ")
    
    # Llama a la función generar_tabla_simbolos para escribir la tabla de símbolos en un archivo
    generar_tabla_simbolos(symbol_table, output_file)
