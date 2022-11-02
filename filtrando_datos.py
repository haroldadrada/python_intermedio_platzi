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
    # Solución con List comprehensions:
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    print("> Lista de todas las personas que saben Python: ")
    for worker in all_python_devs:
        print(worker)
    

    # 2. Lista que obtenga todos los nombres de las personas que trabajan en Platzi
    # Solución con List comprehensions:
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    print("> Lista de todas las personas que trabajan en Platzi: ")
    for worker in all_platzi_workers:
        print(worker)

    # 3. Lista que obtenga todos los mnombres de las personas adultas
    # Solución con filter y map:
    adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))

    print("> Lista de todas las personas que son mayores de edad: ")
    print("- Usando filter y map: ")
    for worker in adults:
        print(worker)

    # Solución usando list comprehensions:
    all_age_works = [worker["name"] for worker in DATA if worker["age"] >= 18]

    print("- Usando List comprehensions: ")
    for worker in all_age_works:
        print(worker)
    
    # 3. Crear lista de diccionarios y que tenga una llave más old, que me dice si una persona es mayor a 70 años o menor
    # Solución con map:
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    print("- Usando map: ")
    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()
