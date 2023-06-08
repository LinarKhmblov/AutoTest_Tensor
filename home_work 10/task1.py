# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


def generate_random_name():
    max_lenght = 15
    min_lenght = 1

    def random_words():
        lenght = random.randint(min_lenght, max_lenght)
        word = ""
        for _i in range(lenght):
            letter = chr(random.randint(97, 112))
            word += letter
        return word

    while True:
        name = random_words() + " " + random_words()
        yield name

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))