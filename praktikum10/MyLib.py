import Globals as g


def panjangString(char):
    sum = 0
    for c in char:
        sum += 1
    return sum


def cariKarakter(search, char):
    if search in char:
        print("Ada")
    else:
        print("Tidak ada")


def frekuensiKarakter(search, char):
    return sum(search == i for i in char)


def cekPalindrom(char):
    return char == char[::-1]
