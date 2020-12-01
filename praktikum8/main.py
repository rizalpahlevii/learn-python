import myLib


def main():
    angka1 = int(input("Masukkan angka pertama untuk aritmatika:"))
    angka2 = int(input("Masukkan angka kedua untuk aritmatika:"))
    s = float(input("Masukkan sisi persegi (float):"))
    a, t = map(float, input("Masukkan a & t segitiga (float)(float):").split())

    print("Hasil Penjumlahan :", myLib.tambah(angka1, angka2))
    print("Hasil Pengurangan :", myLib.kurang(angka1, angka2))
    print("Hasil Perkalian :", myLib.kali(angka1, angka2))
    print("Hasil Pembagian :", myLib.bagi(angka1, angka2))
    print("Luas Persegi :", myLib.luasPersegi(s))
    print("Luas Segitiga :", myLib.luasSegitiga(a, t))


main()
