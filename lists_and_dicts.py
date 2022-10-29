# Listas y diccionarios anidados

def run():
    my_list = [1, "Hola", True, 4.5]
    my_dict = {"firstname": "Harold", "lastname": "Adrada"}

    # Lista de diccionarios
    super_list = [
        {"firstname": "Harold", "lastname": "Adrada"},
        {"firstname": "Beatriz", "lastname": "Adrada"},
        {"firstname": "Alejandro", "lastname": "Adrada"},
        {"firstname": "Gloria", "lastname": "Gómez"},
        {"firstname": "José Felipe", "lastname": "Galvis"},
    ]

    # Diccionario de listas
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 2.2, 3.3, 4.4]
    }

    for key, value in super_dict.items():
        print(key, "=>", value)
    
    for element in super_list:
        for key, value in element.items():
            print(key, "=>", value)


if __name__ == '__main__':
    run()
