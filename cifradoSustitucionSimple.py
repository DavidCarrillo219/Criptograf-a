# Cifra de Sutituión Simple

import pyperclip, sys, random

LETRAS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def main():
    print("""\nElije una opcion:
          1. Cifrar
          2. Descifrar
          3. Generar clave""")
    opcion = int(input('\nOpcion > '))

    # Menu de opciones
    if opcion == 1:
        modo = 'cifrado'
        mensaje = input('Mensaje > ')
        clave = input ('Clave > ')
        comprobarClave(clave)
        texto = cifrarMensaje(clave, mensaje)

    elif opcion == 2:
        modo = 'descifrado'
        mensaje = input('Mensaje > ')
        clave = input ('Clave > ')
        texto = descifrarMensaje(clave, mensaje)
        comprobarClave(clave)

    elif opcion == 3:
        clave = claveAleatoria()
        print('Clave: ', clave)
        sys.exit()

    # Impresión del texto llano o criptograma

    print('\nClve %s' % (clave))
    print('El mensaje %s es:' % (modo))
    print('  ',texto)
    pyperclip.copy(texto)
    print()
    print('El mensaje se ha copiado al portapapeles.')

def comprobarClave(clave):
    listaClave = list(clave)
    listaLetras = list(LETRAS)
    listaClave.sort()
    listaLetras.sort()
    if listaClave != listaLetras:
        print('Clave incorrecta.')
        sys.exit()

def cifrarMensaje(clave,mensaje):
    return mensajeCod(clave, mensaje, 'cifrar'). upper()

def descifrarMensaje(clave, mensaje):
    return mensajeCod(clave, mensaje, 'descifrar').lower()

def mensajeCod(clave, mensaje, modo):
    texto = ''
    carsA = LETRAS
    carsB = clave
    if modo == 'descifrar':
        # Para descifrar es el mismo codigo que para cifrar.
        # Solo se intercambia clave y LETRAS.
        carsA, carsB = carsB, carsA

    # Se recorre uno a uno cada simbolo del mensaje}
    for simbolo in mensaje:
        if simbolo.upper() in carsA:
            # cifrar/descifrar el simbolo
            Indice = carsA.find(simbolo.upper())
            if simbolo.isupper():
                texto += carsB[Indice].upper()
            else:
                texto += carsB[Indice].lower()
        else:
            # si el simbolo no esta en LETRAS, se añade
            texto += simbolo

    return texto

def claveAleatoria():
    clave = list(LETRAS)
    random.shuffle(clave)
    return ''.join(clave)

if __name__ == '__main__':
    main()