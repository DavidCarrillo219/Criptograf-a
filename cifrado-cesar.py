# Cifrado César
print(""" Este programa cifra o descifra un mensaje mediante la cifra César \n""")

import pyperclip

# Símbolos que pueden cifrarse
ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# Almacena la cadena cifradaa/descifrada
salida = ''

# Guardar la opcion deseada
modo = input('¿Deseas cifrar o descrifrar? (c/d) ')

# Se almacena el texto y la clave
texto = input('Introduce el texto: ')
clave = int(input('Y la clave (1-25): '))

# Ejecuta el proceso letra a letra
for simbolo in texto.upper():
    if simbolo in ALFABETO:
        # Identificar la posición de cada símbolo
        pos = ALFABETO.find(simbolo)
        # Ejecuta la operación de cifrado/descifrado
        if modo == 'c':
            pos = (pos + clave) % 26
        elif modo == 'd':
            pos = (pos - clave) % 26
        
        # Añade el nuevo símbolo a la cadena
        salida += ALFABETO[pos]

    # Añade a la cadena el símbolo sin cifrar ni descifrar
    # por que no está en el ALFABETO
    else:
        salida += simbolo

# Imprime en pantalla el resultado
print(salida)

# Copia el mensaje al portapapeles
pyperclip.copy(salida)
