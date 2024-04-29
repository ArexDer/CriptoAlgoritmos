from itertools import permutations
#La librería itertools en Python proporciona funciones para trabajar con iteradores de manera eficiente
#permutations es una función de esta librería que genera todas las posibles permutaciones de un conjunto de elementos.

def permutaciones_palabra(palabra):
    # OBTIENE LAS PERMUTACIONES  DEL SMS
    perm = permutations(palabra)

    # SE LAS PASA A UNA LISTA DE PALABRAS
    palabras_permutadas = [''.join(p) for p in perm]

    # ORDENARO CON SORT.
    palabras_permutadas.sort()

    # CANTI DE PERMUTACIONES.
    num_permutaciones = len(palabras_permutadas)

    # MOSTRrar el numero de resultados
    print("Número total de permutaciones:", num_permutaciones)

    # SOLO LOS PRIMERO 10
    print("\nLas 10 primeras permutaciones ordenadas alfabéticamente:")
    for i in range(min(10, num_permutaciones)):
        print(palabras_permutadas[i])

#INCIO DE EJECUCION EN CONSOLA.............................................................
# Pedir al usuario la palabra
palabra = input("Ingresa una palabra sin espacios para encontrar sus permutaciones: ")

# Llamar a la función para obtener permutaciones y mostrar resultados
permutaciones_palabra(palabra)
