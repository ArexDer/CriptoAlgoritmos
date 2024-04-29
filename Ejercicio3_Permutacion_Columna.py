def cifrado_permutacion_columnas(mensaje, n):
    # Eliminar espacios del mensaje y obtener su longitud sin espacios
    mensaje_sin_espacios = mensaje.replace(" ", "")
    longitud_mensaje = len(mensaje_sin_espacios)
    
    # Verificar que la longitud del mensaje sin espacios no supere el límite de la matriz
    if longitud_mensaje > n * n:
        print("Error: EL MENSAJE SUPERA A LA MATRIZ.")
        return

    # Calcular el número de espacios adicionales necesarios para completar la matriz
    espacios_adicionales = n * n - longitud_mensaje

    # Llenar el mensaje con '*' para completar la matriz
    mensaje_completo = mensaje_sin_espacios + '*' * espacios_adicionales

    # Crear la matriz de cifrado
    matriz_cifrado = [mensaje_completo[i:i+n] for i in range(0, n*n, n)]

    # Transponer la matriz para realizar la permutación de columnas
    matriz_cifrado = [list(columna) for columna in zip(*matriz_cifrado)]

    # Imprimir la matriz de cifrado
    print("MATRIZ de cifrado:")
    for fila in matriz_cifrado:
        print(''.join(fila))

    # Mensaje original
    print("\SMS original:", mensaje)

    # Mensaje cifrado
    mensaje_cifrado = ''.join([''.join(fila) for fila in matriz_cifrado])
    print("SMS cifrado:", mensaje_cifrado)

# Pedir al usuario el mensaje y el número de columnas
mensaje = input("Ingresa el mensaje a cifrar (sin espacios): ")
n = int(input("Ingresa el número de columnas para la matriz de cifrado: "))

# EJECUCION......
cifrado_permutacion_columnas(mensaje, n)
