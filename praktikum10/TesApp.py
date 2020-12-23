import Globals
from MyLib import *


def main():

    data = "balonku ada lima, rupa-rupa warnanya"

    c1 = str(input())
    c2 = str(input())
    p = str(input())

    print(panjangString(data))
    cariKarakter(c1, data)
    print(frekuensiKarakter(c2, data))
    if cekPalindrom(p):
        print("Palindrom")
    else:
        print("Bukan Palindrom")


if __name__ == "__main__":
    main()
