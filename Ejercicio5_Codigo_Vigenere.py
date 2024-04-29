def cifrado_vigenere(cadena, clave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    n = len(alfabeto)
    
    # CLAVE = LONGITUD DE LA CADENA
    clave_ajustada = clave * (len(cadena) // len(clave)) + clave[:len(cadena) % len(clave)]

    # CIFRADO DE LOS DATOS
    resultado = ''
    for i in range(len(cadena)):
        if cadena[i] in alfabeto:
            index_cadena = alfabeto.index(cadena[i])
            index_clave = alfabeto.index(clave_ajustada[i])
            index_cifrado = (index_cadena + index_clave) % n
            resultado += alfabeto[index_cifrado]
        else:
            resultado += cadena[i]

    # Mostrar resultados
    print("Cadena de caracteres original   :", cadena)
    print("Clave de cifrado                :", clave)
    print("Cadena de caracteres cifrada    :", resultado)

# Pedir al usuario la cadena de caracteres y la clave de cifrado
cadena = input("Ingresa la cadena de caracteres a cifrar: ").lower()
clave = input("Ingresa la clave de cifrado: ").lower()

# EJECUCION...
cifrado_vigenere(cadena, clave)
