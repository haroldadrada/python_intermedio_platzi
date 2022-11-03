"""
1. Crear las listas all_python_devs y all_platzi_workers usando una combinación de filter y map.
2. Crear la lista old_people y adults con list comprehensions
"""

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Harold',
        'age': 36,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # 1. Lista que obtenga todos los nombres de las personas que saben Python
    # Solución con combinacion de filter y map:
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    print(">> Lista de todas las personas que saben Python. (Uso de filter y map): ")
    for worker in all_python_devs:
        print(worker)

    # 2. Lista que obtenga todos los nombres de las personas que trabajan en Platzi
    # Solución con combinacion de filter y map:
    all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))

    print(">> Lista de todas las personas que trabajan en Platzi. (Uso de filter y map): ")
    for worker in all_platzi_workers:
        print(worker)

    # 3. Lista que obtenga todos los nombres de las personas adultas, mayores de 18 años
    # Solución con list comprehensions:
    adults = [worker["name"] for worker in DATA if worker["age"] > 18]

    print(">> Lista de todas las personas adultas, mayores de 18 años. (Uso de list comprehensions): ")
    for worker in adults:
        print(worker)

    # 4. Crear lista: Agregar Diccionario(old) a la lista DATA, y que guarde en el valor si las personas son mayores(True) o menores(False) de 70 años
    # Solución con list comprehensión:
    old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]

    print(">> List Old People. (Uso de list comprehensions): ")
    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()
