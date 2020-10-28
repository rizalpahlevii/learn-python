panjang = float(input("Masukkan panjang : "))
lebar = float(input("Masukkan lebar : "))
opsi = str(input("Pilih opsi antara 'setuju' dan 'tidak setuju' : "))

luasTanah = panjang * lebar
print("Luas Tanah : ", luasTanah)
if (opsi == "setuju"):
    print(luasTanah / 2)
else:
    print(luasTanah)
