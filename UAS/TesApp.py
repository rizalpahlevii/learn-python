# Muhammad Rizal Pahlevi
# A11.2020.12692
# 4110

import MyLib


def main():
    nim = input("NIM : ")
    nama = input("Nama : ")

    totalMataKuliah = int(input('Jumlah mata kuliah: '))
    if totalMataKuliah > 10:
        print('Tidak boleh melebihi 10')
        exit()
    g.totalMataKuliah = totalMataKuliah

    mataKuliah = [str] * totalMataKuliah
    for i in range(totalMataKuliah):
        mataKuliah[i] = input()

    nilai = [int] * totalMataKuliah
    for j in range(totalMataKuliah):
        nilai[j] = int(input())
    MyLib.displayTranskrip(nim, nama, mataKuliah, nilai)


if __name__ == "__main__":
    main()
