
kode = input("Masukkan kode baju :")
if kode == "A":
    merk_baju = "Dancow"
    ukuran = input("Input Ukuran : ")
    if ukuran == "250":
        harga = 30000
    elif ukuran == "500":
        harga = 55000
    else:
        harga = 95000

    jumlah = int(input("Masukkan jumlah : "))
    diskon = 0
    if jumlah > 3:
        diskon = (harga * jumlah) * 0.10

    tagihan = (harga * jumlah) - diskon
    print("Merk", merk_baju)
    print("Ukuran", ukuran)
    print("Tagihan", tagihan)

elif kode == "B":
    merk_baju = "Morinaga"
    ukuran = input("Input Ukuran : ")
    if ukuran == "250":
        harga = 850000
    elif ukuran == "500":
        harga = 160000
    else:
        harga = 280000

    jumlah = int(input("Masukkan jumlah : "))
    diskon = 0
    if jumlah > 3:
        diskon = (harga * jumlah) * 0.20

    tagihan = (harga * jumlah) - diskon
    print("Merk", merk_baju)
    print("Ukuran", ukuran)
    print("Tagihan", tagihan)

elif kode == "C":
    merk_baju = "Bebelac"
    ukuran = input("Input Ukuran : ")
    if ukuran == "250":
        harga = 110000
    elif ukuran == "500":
        harga = 200000
    else:
        harga = 390000

    jumlah = int(input("Masukkan jumlah : "))
    diskon = 0
    if jumlah > 3:
        diskon = (harga * jumlah) * 0.25

    tagihan = (harga * jumlah) - diskon
    print("Merk", merk_baju)
    print("Ukuran", ukuran)
    print("Tagihan", tagihan)

elif kode == "D":
    merk_baju = "SGM"
    ukuran = input("Input Ukuran : ")
    if ukuran == "250":
        harga = 25000
    elif ukuran == "500":
        harga = 45000
    else:
        harga = 85000

    jumlah = int(input("Masukkan jumlah : "))
    diskon = 0
    if jumlah > 3:
        diskon = (harga * jumlah) * 0.10

    tagihan = (harga * jumlah) - diskon
    print("Merk", merk_baju)
    print("Ukuran", ukuran)
    print("Tagihan", tagihan)
elif kode == "E":
    merk_baju = "Lactogrow"
    ukuran = input("Input Ukuran : ")
    if ukuran == "250":
        harga = 950000
    elif ukuran == "500":
        harga = 175000
    else:
        harga = 315000

    jumlah = int(input("Masukkan jumlah : "))
    diskon = 0
    if jumlah > 3:
        diskon = (harga * jumlah) * 0.25

    tagihan = (harga * jumlah) - diskon
    print("Merk", merk_baju)
    print("Ukuran", ukuran)
    print("Tagihan", tagihan)

else:
    print("Ada kesalahan! Kode barang salah")
