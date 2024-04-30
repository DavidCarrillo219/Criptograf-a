# Crifra afín

import sys, pyperclip, criptomat, random

SIMBOLOS = """!¡"#$%&'()*+,-./0123456789:;<=>¿?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ
                [\]^_`abcdefghijklmnñopqrstuvwxyz{|}~"""

def main():
    print('\n¿Qué deseas hacer?')
    print('\n1- Cifrar')
    print('2- Descifrar')
    print('3- Generar clave')

    # Guardar la opcion deseada
    modo = input('\nOpcion (1, 2, 3) > ')

    if modo == '1': # Cifrar
        texto = input('\nMensaje: ')
        clave_A = int(input('Constante de decimación (2-96): '))
        clave_B = int(input('Constante de desplazamiento (0-96): '))
        mensaje = cifrar_mensaje(texto, clave_A, clave_B)

    elif modo == '2': # Descifrar
        texto = input('\nCriptograma: ')
        clave_A = int(input('Constante de decimación (2-96): '))
        clave_B = int(input('Constante de desplazamiento (0-96): '))
        mensaje = decifrar_mensaje(texto, clave_A, clave_B)

    elif modo == '3': # Clave Aleatoria
        clave = generar_clave()
        print('\nClave: ', clave)
        sys.exit()

    else:
        print('Opcion invalida')
        sys.exit()

    print('\nMensaje: ')
    print(mensaje)
    pyperclip.copy(mensaje)
    print('\nMensaje copiado al portapapeles.')

def generar_clave():
    while True:
        clave_A = random.randint(2, len(SIMBOLOS))
        clave_B = random.randint(2, len(SIMBOLOS))
        if criptomat.mcd(clave_A, len(SIMBOLOS)) == 1:
            return (clave_A, clave_B)
        

def revisar_clave(clave_A, clave_B):
    if clave_A not in range(2, 97):
        print('La constante de decimación ha de estar en rango [2, 96].')
        sys.exit()
    if clave_B not in range(0, 97):
        print('La constante de desplazamiento ha de estar en rango [0, 96].')
        sys.exit()
    if criptomat.mcd(clave_A, len(SIMBOLOS)) != 1:
        print('La clave A (%s) y la longitud del alfabeto (%s) no son coprimos.' % (clave_A, len(SIMBOLOS)))
        sys.exit()

def cifrar_mensaje(texto, clave_A, clave_B):
    revisar_clave(clave_A, clave_B)
    criptograma = ''
    for simbolo in texto:
        if simbolo in SIMBOLOS:
            # cifrar el simbolo
            indice = SIMBOLOS.find(simbolo)
            criptograma += SIMBOLOS[(indice * clave_A + clave_B) % len(SIMBOLOS)]
        else:
            criptograma += simbolo # se añade sin cifrar
    return criptograma


def decifrar_mensaje(texto, clave_A, clave_B):
    revisar_clave(clave_A, clave_B)
    texto_plano = ''
    inverso_A = criptomat.invMod(clave_A, len (SIMBOLOS))
    for simbolo in texto:
        if simbolo in SIMBOLOS:
            # descifrar el simbolo
            indice = SIMBOLOS.find(simbolo)
            texto_plano += SIMBOLOS[(indice - clave_B) * inverso_A % len(SIMBOLOS)]
        else:
            texto_plano  += simbolo # se añade sin descifrar
    return texto_plano

if __name__ == '__main__':
    main()