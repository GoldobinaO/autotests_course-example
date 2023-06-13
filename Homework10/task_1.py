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


def gen_word(end):
    word = ""
    for i in range(end):
        word += random.choice("abcdefghijklmnopqrstuvwxyz")
    return word


def generate_random_name():
    while True:
        len_1 = random.randint(1, 15)
        len_2 = random.randint(1, 15)
        yield f"{gen_word(len_1)} {gen_word(len_2)}"


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
