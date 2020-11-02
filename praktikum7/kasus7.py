import random
saldo = int(input("Masukkan saldo awal : "))
tanggal_lahir = int(input("Kapan tanggal lahir mama : "))

if tanggal_lahir == 12:
    request_pulsa = int(
        input("Masukkan jumlah pulsa yang di inginkan mama : "))

    signal = 0
    percobaan = 0

    while signal < 0.5:
        print("Mohon tunggu .....")
        percobaan += 1
        if percobaan >= 3:
            print("Transaksi Gagal!")
            exit()

        signal = random.random()

    if saldo > request_pulsa:
        print("Transaksi", request_pulsa, 'Berhasil')
    else:
        print("Saldo tidak cukup!")


else:
    print("Anda Penipu!")
