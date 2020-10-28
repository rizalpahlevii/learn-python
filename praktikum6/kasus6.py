saldo = int(input("Saldo : "))
while True:
    n = int(input("Pengeluaran soni hari ini (isikan -1 untuk keluar) : "))
    if(n == -1):
        break

    cek = saldo - n
    if saldo - n >= 0:
        saldo = saldo - n
    else:
        print("Saldo tidak cukup")
        break

print("Sisa saldo ", saldo)
