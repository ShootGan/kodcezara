import random
import os

alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"


# odszyfrowane = ""
# szyfr =input("wprowadz szyfr: ")
def main():
    print("zakoduj[1]")
    print("odkoduj[2]")
    print("exit[0]")
    option = input('Wybierz:')
    print(option)
    while option != 0:
        if option == '1':
            text = input('Podaj tekst:')
            key = input('Podaj klucz lub enter dla losowego:')
            encryption(text, key)
        elif option == '2':
            text = input('Podaj tekst:')
            unencryption(text)
        else:
            main()


def encryption(text, key):
    text = text.lower()
    if not key:
        key = (random.randint(1, 35))
    output = ''
    for x in text:
        if x in alphabet:
            number = (alphabet.index(x) + int(key))
            if number > 35:
                number = number - 35
            output = output + alphabet[number]
        else:
            output = output + x

    print(output)
    input("Enter żeby kontynuować")
    main()


def unencryption(code):
    cz = []
    code = code.lower()
    output = ''
    for leter in alphabet:
        cz.append(code.count(leter))
    key = cz.index(max(cz))
    for x in code:
        if x in alphabet:
            output = output + alphabet[alphabet.index(x) - key]
        else:
            output = output + x
    print(output)
    input("Enter żeby kontynuować")
    main()


# print(odszyfrowane)

if __name__ == '__main__':
    main()
