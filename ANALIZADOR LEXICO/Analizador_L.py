import re

def analizador_lexico(cadena):
    tokens = []
    pos = 0

    while pos < len(cadena):
        # Ignorar espacios en blanco
        if cadena[pos].isspace():
            pos += 1
            continue

        # Identificador: letra(letra|digito)*
        if cadena[pos].isalpha():
            identificador = cadena[pos]
            pos += 1

            while pos < len(cadena) and (cadena[pos].isalpha() or cadena[pos].isdigit()):
                identificador += cadena[pos]
                pos += 1

            tokens.append(('IDENTIFICADOR', identificador))
            continue

        # Número Real: entero.entero+
        if cadena[pos].isdigit():
            entero = cadena[pos]
            pos += 1

            while pos < len(cadena) and cadena[pos].isdigit():
                entero += cadena[pos]
                pos += 1

            if pos < len(cadena) and cadena[pos] == '.':
                entero += '.'
                pos += 1

                while pos < len(cadena) and cadena[pos].isdigit():
                    entero += cadena[pos]
                    pos += 1

                tokens.append(('REAL', float(entero)))
                continue
            else:
                tokens.append(('ENTERO', int(entero)))
                continue

        # Caracteres no reconocidos
        tokens.append(('DESCONOCIDO', cadena[pos]))
        pos += 1

    return tokens

# Ejemplo de uso
#entrada = "abc 123 45.67 x_y 89.01"
entrada = (input("ingresa caracteres: "))
resultado = analizador_lexico(entrada)

for token in resultado:
    print(token)
