import re

def main():
    # Pedir la gramática al usuario
    print("Ingrese la gramática:")
    grammar = input()

    # Analizar la entrada de usuario
    grammar_rules = parse_grammar(grammar)
    if grammar_rules is None:
        print("Gramática no válida.")
        return

    # Leer la entrada a analizar
    print("Ingrese la entrada a analizar:")
    input_text = input()

    # Analizar la entrada
    result = parse_input(input_text, grammar_rules)

    # Guardar los resultados en un archivo de texto
    with open("output.txt", "w") as file:
        file.write(result)
    print("Resultados guardados en 'output.txt'.")

def parse_grammar(grammar):
    """
    Analiza la gramática ingresada por el usuario y la convierte en un diccionario de reglas.
    """
    grammar_rules = {}
    rules = grammar.split(";")
    for rule in rules:
        parts = rule.split("=")
        if len(parts) != 2:
            return None
        lhs = parts[0].strip()
        rhs = parts[1].strip()
        grammar_rules[lhs] = rhs
    return grammar_rules

def parse_input(input_text, grammar_rules):
    """
    Analiza la entrada según la gramática proporcionada y devuelve el resultado.a
    """
    # Regex para identificar símbolos
    id_pattern = r'[a-zA-Z][a-zA-Z0-9]*'
    int_pattern = r'\d+'
    real_pattern = r'\d+\.\d+'
    operator_pattern = r'[+\-*/=<>!&|]'
    punctuation_pattern = r'[();{}]'

    # Agregar palabras reservadas
    keywords = {'if', 'while', 'return', 'else', 'int', 'float'}

    # Analizar la entrada
    tokens = re.findall(f'{id_pattern}|{int_pattern}|{real_pattern}|{operator_pattern}|{punctuation_pattern}', input_text)

    # Verificar la sintaxis
    result = ""
    for token in tokens:
        if token in keywords:
            result += f"{token}: Palabra reservada\n"
        elif re.match(id_pattern, token):
            result += f"{token}: Identificador\n"
        elif re.match(int_pattern, token):
            result += f"{token}: Entero\n"
        elif re.match(real_pattern, token):
            result += f"{token}: Real\n"
        elif re.match(operator_pattern, token):
            result += f"{token}: Operador\n"
        elif re.match(punctuation_pattern, token):
            result += f"{token}: Puntuación\n"
        else:
            result += f"{token}: No reconocido\n"
    return result

if __name__ == "__main__":
    main()
