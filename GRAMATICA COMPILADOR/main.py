import analizador
print ("--------------------------------------------")
texto = input("Ingresa el texto que quieres analizar: ")
print ("--------------------------------------------")
analizador = analizador.AnalizadorLexico()
analizador.analizador(texto)
analizador.getListaTokens()
print ("--------------------------------------------")
print("Esta es la salida bro")
print ("--------------------------------------------")
analizador.imprimirSalida()
print ("--------------------------------------------")
print("La pila es la siguiente bro")
print ("--------------------------------------------")
analizador.imprimirSintactico()
print ("--------------------------------------------")