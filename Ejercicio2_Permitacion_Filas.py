def cifrado_permutacion_filas(mensaje, n):
    # Eliminar espacios del mensaje y obtener su longitud sin espacios
    mensaje_sin_espacios = mensaje.replace(" ", "")
    longitud_mensaje = len(mensaje_sin_espacios)
    
    # Verificar que la longitud del mensaje sin espacios no supere el límite de la matriz n x n
    if longitud_mensaje > n * n:
        print("Error: La longitud del mensaje supera el límite de la matriz.")
        return

    # Calcular el número de espacios adicionales necesarios para completar la matriz
    espacios_adicionales = n * n - longitud_mensaje

    # Llenar el mensaje con '*' para completar la matriz
    mensaje_completo = mensaje_sin_espacios + '*' * espacios_adicionales

    # Crear la matriz de cifrado
    matriz_cifrado = [mensaje_completo[i:i+n] for i in range(0, n*n, n)]

    # Imprimir la matriz de cifrado
    print("Matriz de cifrado:")
    for fila in matriz_cifrado:
        print(fila)

    # Mensaje original
    print("\nMensaje original:", mensaje)

    # Mensaje cifrado
    mensaje_cifrado = ''.join([''.join(fila) for fila in matriz_cifrado])
    print("Mensaje cifrado:", mensaje_cifrado)

# Pedir al usuario el mensaje y el número de filas
mensaje = input("Ingresa el mensaje a cifrar (sin espacios): ")
n = int(input("Ingresa el número de filas para la matriz de cifrado: "))

# Llamar a la función para cifrar el mensaje y mostrar resultados
cifrado_permutacion_filas(mensaje, n)
