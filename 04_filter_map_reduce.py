from functools import reduce


"""
Funciones de orden superior(High order functions:
filter, map y reduce
"""


def run():
    # *** Función de orden superior: filter ***
    # Ejemplo 1: De la siguiente lista, obtener los impares
    print("> Ejemplo 1: ")
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    # Solución ejemplo 1, utilizando list comprehensions:
    list_impares = [i for i in my_list if i % 2 != 0]
    print(f"List comprehensions => {list_impares}")

    # Solución ejemplo 1, utilizando filter:
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    print(f"Filter => {odd}")

    # Ejemplo 2: De la siguiente lista, convertirla a otra lista pero con los números elevandos al cuadrado
    print("> Ejemplo 2: ")
    my_list_dos = [1, 2, 3, 4, 5]

    # Solución ejemplo 2, utilizando list comprehensions:
    list_cuadrado = [i**2 for i in my_list_dos]
    print(f"List comprehensions => {list_cuadrado}")

    # Solución ejemplo 2, utilizando map:
    odd = list(map(lambda x: x**2, my_list_dos))
    print(f"Map => {odd}")

    # Ejemplo 3: De la siguiente lista, multiplicar consecutivamente los elementos
    print("> Ejemplo 3: ")
    my_list_tres = [2, 2, 2, 2, 2]

    # Solución ejemplo 3, utilizando ciclos:
    all_multiplied = 1
    for i in my_list_tres:
        all_multiplied = all_multiplied*i

    print(f"Ciclo for => {all_multiplied}")

    # Solución ejemplo 3, utilizando reduce:
    multiplied = reduce(lambda a, b: a * b, my_list_tres)

    print(f"Reduce => {multiplied}")


if __name__ == '__main__':
    run()
