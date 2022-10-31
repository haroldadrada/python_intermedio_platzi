"""
Reto: Crear, con un list comprehensions, una lista
de todos los múltiplos de 4 que a la vez también 
son múltiplos de 6 y de 9, hasta 5 dígitos.
"""

def run():
    # Forma larga
    multiples = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(multiples)

    print("="*20)

    # Forma corta
    multiples_new = [i for i in range(1, 100000) if i % 36 == 0]
    print(multiples_new)


if __name__ == '__main__':
    run()