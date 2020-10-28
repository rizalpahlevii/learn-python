n = int(input("Masukkan angka : "))

if n >= 2:
    prima = True
    for i in range(2, n):
        if n % i == 0:
            prima = False

    if prima:
        print(n, "Bilangan prima")
    else:
        print(n, "Bukan Bilangan prima")
else:
    print(n, "Bukan Bilangan prima")
