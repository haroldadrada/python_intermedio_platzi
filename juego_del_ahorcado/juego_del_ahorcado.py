import random
import os


def read_data():
    with open("./archivos/data.txt", "r", encoding="utf-8")as f:
        words = [line.strip().upper() for line in f]
    return words


def run():
    data = read_data()
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"]*len(chosen_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
    while True:
        os.system("cls")  # Si estás en Unix (Mac o Linux) cambia cls por clear
        print("¡Adivina la palabra!")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter

        if "_" not in chosen_word_list_underscores:
            # Si estás en Unix (Mac o Linux) cambia cls por clear
            os.system("cls")
            print("¡Ganaste! La palabra era:", chosen_word)
            break


if __name__ == '__main__':
    run()
