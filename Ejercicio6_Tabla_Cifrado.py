def imprimir_tabla(tabla):
    for fila in tabla:
        print(' '.join(fila))


def cifrado_tabla(cadena, tabla):
    resultado = ''
    for letra in cadena:
        encontrado = False
        for fila in tabla:
            if letra in fila:
                resultado += fila[0]
                encontrado = True
                break
        if not encontrado:
            resultado += '**'
    return resultado

# Definir la tabla de cifrado
tabla_cifrado = [
    ['*', 'A', 'S', 'D', 'F', 'G'],
    ['Q', 'a', 'b', 'c', 'd', 'e'],
    ['W', 'f', 'g', 'h', 'i', 'j'],
    ['E', 'k', 'l', 'm', 'n', 'o'],
    ['R', 'p', 'q', 'r', 's', 't'],
    ['T', 'u', 'v', 'x', 'y', 'z']
]

# VISUALIZAO MI TABLA
print("Tabla de cifrado:")
imprimir_tabla(tabla_cifrado)

# Pedir al usuario la cadena de caracteres
cadena = input("Ingresa la cadena de caracteres a cifrar: ")

cadena =cadena.lower()
#EJECUCION....
# Realizar el cifrado utilizando la tabla y mostrar resultado

resultado_cifrado = cifrado_tabla(cadena, tabla_cifrado)
print("\nMensaje original   :", cadena)
print("Mensaje cifrado    :", resultado_cifrado)
