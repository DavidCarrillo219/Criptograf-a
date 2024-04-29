# cifrado atbash
import pyperclip

# Alfabetos empleados

claro =   "abcdefghijklmnñopqrstuvwxyz"
cifrado = "ZYXWVUTSRQPOÑNMLKJIHGFEDCBA"

# Almacena la forma cifrado/descifrado del texto
salida = ''

# Guarda el texto introducido 

texto = input("Introduce un texto: ")

# Ejecuta el cifrado/ descifrado letra a letra
for simbolo in texto.lower():
    if simbolo in claro:
        # Identifica la posicion de cada simbolo
        indice = claro.index(simbolo)
        # Añade un nuevo simbolo al texto cifrado/descifrado
        salida += cifrado[indice]




# Imprime en pantalla el resultado
print(salida)

# Copia el mensaje al portapapeles
pyperclip.copy(salida)
