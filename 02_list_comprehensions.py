def run():
    # Ejemplo 1: crear una lista con los primeros 100 números naturales al cuadrado

    # # Ejemplo 1 resuelto de forma tradicional:
    # squares = []
    # for i in range(1, 101):
    #     squares.append(i**2)

    # print(squares)

    # Ejemplo 1 resuelto con lists comprehensions:
    squares_lc = [i**2 for i in range(1, 101)]
    print(squares_lc)

    # # Ejemplo 2: crear una lista con los primeros 100 números naturales al cuadrado que no sean divisibles entre tres
    
    # # Ejemplo 2 resuelto de forma tradicional:
    # squares_not_three = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares_not_three.append(i**2)

    # print(squares_not_three)

    # Ejemplo resuelto con lists comprehensions:
    squares_not_three_lc = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares_not_three_lc)


if __name__ == '__main__':
    run()
