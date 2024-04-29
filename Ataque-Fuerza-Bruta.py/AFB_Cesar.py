# Recuperar la clave de una cifra César por fuerza bruta

ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# Almacena el criptograma
criptograma = input('Criptograma: ')

# Recoger una a una todas las claves (1-25)
for clave in range(1,len(ALFABETO)):

    # Almacena la cadena descifrada
    salida = ''
    for simbolo in criptograma:
        if simbolo in ALFABETO:
            pos = ALFABETO.find(simbolo)
            # Descifra el carácter
            pos = (pos - clave) % len(ALFABETO)

            # Añade el símbolo descifrado a la cadena
            salida += ALFABETO[pos]

            # Si hay un espacio u otro caracter no 
            # alfabético la añade a la cadena sin tocar
        else:
            salida  += simbolo

    # Imprime en pantalla el resultado completo
    print ('Clave %d: %s' % (clave,salida))