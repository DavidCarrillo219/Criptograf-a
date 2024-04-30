# Cifrador trnasposicion columnar simple

import  pyperclip

def main():
    mensaje = input('Introduce el mensaje: ')
    clave = int(input('y la clave númerica: '))
    mensaje = eliminar_espacios(mensaje)

    criptograma = salida(cifrar(mensaje,clave))

    # Imprime en pantalla el criptograma
    print(criptograma.upper())
    # Y lo copia al portapapeles
    pyperclip.copy(criptograma)

# Elimina espacios en blanco en el mensaje
def eliminar_espacios(mensaje):
    mensaje_nuevo = ''
    for simbolo in mensaje:
        if simbolo != ' ':
            mensaje_nuevo += simbolo
    return mensaje_nuevo

# Agrupar las letras en grupos de 5
def salida (criptograma):
    BLOQUE = 5
    texto = ''
    for i in range(len(criptograma)):
        if (i+1) % BLOQUE != 0:
            texto += criptograma[i]
        else:
            texto += criptograma[i]+' '
    return texto

def cifrar(mensaje,clave):
    # Cada cadena del criptograma es una columna de la lista
    criptograma =[''] * clave

    # Recorremos cada columna de la tabla
    for col in range(clave):
        pos = col

        # En cada columna añadiremos las letras hasta
        # que pos sobrepase la longitud del mensaje

        while pos < len(mensaje):
            criptograma[col] += mensaje[pos]

            # desplazamos la posicion
            pos += clave

    # Convertimos la lista en una única cadena
    return ''.join(criptograma)

# Si se ejecuta el programa (en vez de importarse)
# se llama a la funcion main() inmediatamente
if __name__ == '__main__':
    main()

        