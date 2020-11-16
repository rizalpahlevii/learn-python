kode = int(input("Masukkan kode baju :"))


if kode == 1:
    merk_baju = "3 Second"
    ukuran = input("Input Ukuran : ")
    if ukuran == "S":
        harga = 200000
    elif ukuran == "M":
        harga = 220000
    else:
        harga = 250000

    jumlah = int(input("Masukkan jumlah : "))
    diskon = 0
    if jumlah > 3:
        diskon = (harga * jumlah) * 0.50

    tagihan = (harga * jumlah) - diskon
    print("Merk", merk_baju)
    print("Ukuran", ukuran)
    print("Tagihan", tagihan)


elif kode == 2:
    merk_baju = "Nevada"
    ukuran = input("Input Ukuran : ")
    if ukuran == "S":
        harga = 170000
    elif ukuran == "M":
        harga = 180000
    else:
        harga = 200000

    jumlah = int(input("Masukkan jumlah : "))
    diskon = 0
    if jumlah > 3:
        diskon = (harga * jumlah) * 0.50

    tagihan = (harga * jumlah) - diskon
    print("Merk", merk_baju)
    print("Ukuran", ukuran)
    print("Tagihan", tagihan)

elif kode == 3:
    merk_baju = "Gucci"
    ukuran = input("Input Ukuran : ")
    if ukuran == "S":
        harga = 200000
    elif ukuran == "M":
        harga = 250000
    else:
        harga = 270000

    jumlah = int(input("Masukkan jumlah : "))
    diskon = 0
    if jumlah > 3:
        diskon = (harga * jumlah) * 0.40

    tagihan = (harga * jumlah) - diskon
    print("Merk", merk_baju)
    print("Ukuran", ukuran)
    print("Tagihan", tagihan)

elif kode == 4:
    merk_baju = "Luis Vuitton"
    ukuran = input("Input Ukuran : ")
    if ukuran == "S":
        harga = 300000
    elif ukuran == "M":
        harga = 300000
    else:
        harga = 350000

    jumlah = int(input("Masukkan jumlah : "))
    diskon = 0
    if jumlah > 3:
        diskon = (harga * jumlah) * 0.35

    tagihan = (harga * jumlah) - diskon
    print("Merk", merk_baju)
    print("Ukuran", ukuran)
    print("Tagihan", tagihan)
elif kode == 5:
    merk_baju = "Kick Denim"
    ukuran = input("Input Ukuran : ")
    if ukuran == "S":
        harga = 100000
    elif ukuran == "M":
        harga = 120000
    else:
        harga = 130000

    jumlah = int(input("Masukkan jumlah : "))
    diskon = 0
    if jumlah > 3:
        diskon = (harga * jumlah) * 0.45

    tagihan = (harga * jumlah) - diskon
    print("Merk", merk_baju)
    print("Ukuran", ukuran)
    print("Tagihan", tagihan)

else:
    print("Ada kesalahan")
    exit
