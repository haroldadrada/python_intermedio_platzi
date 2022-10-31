"""
Reto: Crear, con un dictionary comprehensions, un diccionario 
cuyas llaves sean los 1000 primeros números naturales con sus
raíces cuadradas como valores.
"""

def run():
    squares = {i: i**0.5 for i in range(1, 11)}
    print(squares)


if __name__ == '__main__':
    run()