n = int(input("Masukkan Jumlah uang : "))

rencana_pengeluaran = 1200000
tiket_biasa = 500000
tiket_vip = 1000000

if n < 1200000:
    print("Input tidak valid")
else:
    sisa = n - rencana_pengeluaran
    if sisa >= tiket_vip:
        print("Soni jadi menonton konser dengan tempat duduk VIP")
    elif sisa >= tiket_biasa:
        print("Soni jadi menonton konser dengan tempat duduk biasa")
    else:
        print("Soni tidak bisa menonton konser karena uang kurang")
