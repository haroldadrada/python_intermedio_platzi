"""
Archivo para programar ejemplos y algunas pruebas
"""


def run():
    # Ejemplo de función de orden superior
    def saludo(func):
        func()

    def hola():
        print("Hola!")

    def adios():
        print("Adios!")

    saludo(hola)


if __name__ == '__main__':
    run()
