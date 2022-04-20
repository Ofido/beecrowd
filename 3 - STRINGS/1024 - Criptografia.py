#https://www.beecrowd.com.br/judge/pt/problems/view/1168
# exceded time

import string


def invert_palavra(palavra:str) -> str:
    return palavra[::-1]

for _ in range(int(input())):
    palavra = input()

    primeira_criptografada = ""
    # primeira passada
    for letra in palavra:
        if string.ascii_letters.find(letra) != -1:
            primeira_criptografada += chr(ord(letra)+3)
            continue
        primeira_criptografada += letra

    # segunda passada
    segunda_criptografada = invert_palavra(primeira_criptografada)

    print(segunda_criptografada)

    terceira_criptografada = segunda_criptografada[:int(round(segunda_criptografada.__len__()/2, 0))]
    # terceira passada
    for index in range(int(round(segunda_criptografada.__len__()/2, 0)),segunda_criptografada.__len__()):
        print(index)
        print(segunda_criptografada[index])
        print(ord(segunda_criptografada[index]))
        print(ord(segunda_criptografada[index])-1)
        print(chr(ord(segunda_criptografada[index])-1))
        terceira_criptografada += chr(ord(segunda_criptografada[index])-1)

    print(terceira_criptografada)
