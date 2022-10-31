def run():
    # Emeplo 1: Crear un diccionario cuyas llaves sean los numeros del 1 al 100 y los valores esos valores elevandos al cubo
    
    # # Ejemplo 1 resuelto de forma tradicional:
    # dicta_cubo = {}
    # for i in range(1, 101):
    #     dicta_cubo[i] = i**3
    
    # print(dicta_cubo)

    # Ejemplo 1 resuelto con Dictionary comprehensions:
    dict_cubo_dc = {i: i**3 for i in range(1, 101)}
    print(dict_cubo_dc)

    print("="*20)

    # Emeplo 2: Mismo ejemplo anterior, pero que muestre los que no sean divisibles entre tres:
    # dict_not_three = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         dict_not_three[i] = i**3
    
    # print(dict_not_three)

    # Ejemplo 2 resuelto con Dictionary comprehensions:
    dict_not_three_dc = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(dict_not_three_dc)


if __name__ == '__main__':
    run()