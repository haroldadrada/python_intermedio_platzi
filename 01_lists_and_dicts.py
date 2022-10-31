# Listas y diccionarios anidados

def run():
    # Lista:
    print("> Lista: ")
    my_list = [1, "Hola", True, 4.5]

    # Diccionario:
    print("> Diccionario: ")
    my_dict = {"firstname": "Harold", "lastname": "Adrada"}
    for key in my_dict:
        print(key, "<=>", my_dict[key])

    # Lista de diccionarios
    print("> Lista de Diccionarios: ")
    super_list = [
        {"firstname": "Harold", "lastname": "Adrada"},
        {"firstname": "Beatriz", "lastname": "Adrada"},
        {"firstname": "Alejandro", "lastname": "Adrada"},
        {"firstname": "Gloria", "lastname": "Gómez"},
        {"firstname": "José Felipe", "lastname": "Galvis"},
    ]

    for element in super_list:
        for key, value in element.items():
            print(key, "=>", value)

    # Diccionario de listas
    print("> Diccionarios de Listas: ")
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 2.2, 3.3, 4.4]
    }

    for key, value in super_dict.items():
        print(key, "=>", value)


if __name__ == '__main__':
    run()
