def cifrado_monoalfabetico_desplazamiento(palabra, n):
    #ALFABERO
    alfabeto_original = 'abcdefghijklmnopqrstuvwxyz'
    
    # SE CREA EL ALFABETO CIFRADO
    alfabeto_cifrado = ''.join([chr(((ord(letra) - 97 + n) % 26) + 97) for letra in alfabeto_original])

    # Cifrar el SMS
    resultado = ''.join([alfabeto_cifrado[(alfabeto_original.index(letra) + n) % 26] if letra in alfabeto_original else letra for letra in palabra])

    # Mostrar resultados
    print("Alfabeto original:", alfabeto_original)
    print("Alfabeto cifrado  :", alfabeto_cifrado)
    print("Cadena de caracteres original:", palabra)
    print("Resultado del cifrado:", resultado)


palabra = input("Ingresa la cadena de caracteres a cifrar: ").lower()
n = int(input("Ingresa el valor de desplazamiento n: "))

#EJECUCION...
cifrado_monoalfabetico_desplazamiento(palabra, n)
