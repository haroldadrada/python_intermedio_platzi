# Ciclo for(para):para estas condición, ejecutar estás instrucciones


# # Ejemplo 1: imprime los números del 1 al 10
# print("Imprime los números del 1 al 10")
# for element in range(1, 11):
#   print(element)


# # Ejemplo 2: imprime los elementos de una lista
# print("Imprime los elementos de una lista:")
# my_list = [1, 3, 5, 7, 9]
# for element in my_list:
#     print(element)

# # Ejemplo 3: imprime los elementos de una tupla
# print("Imprime los elementos de una tupla: ")
# my_tuple = ("Harold", "Andrés", "Adrada", "Gómez")
# for element in my_tuple:
#     print(element)

# # Ejemplo 4: imprime los elementos llave/valor de un diccionario
# print("Imprime los elementos llave/valor de un diccionario")
# product = {
#     "name": "Camisa",
#     "price": 15000,
#     "stock": 23
# }
# print("> Primera forma: ")
# for key in product:
#     print(f"{key} => ", product[key])

# print("> Segunda forma: ")
# for key, value in product.items():
#     print(key, "=>", value)

# print("> Tercera forma: ")
# for element in product.items():
#     print(element)

# Ejemplo 5: Lista de diccionarios
people = [
    {
        "name": "Harold Andrés",
        "age": 36
    },
    {
        "name": "José Felipe",
        "age": 2
    },
    {
        "name": "Alejo",
        "age": 30
    }
]

print("> Primera forma: ")
for person in people:
    print(person)

print("> Segunda forma: ")
for person in people:
    print("name => ", person["name"])

# # Ejemplo: 
# al_cuadrado = []
# for elemento in range(1, 11):
#     al_cuadrado.append(elemento**2)

# print(al_cuadrado)
