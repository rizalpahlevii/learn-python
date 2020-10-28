# Kasus 1- Copy Cat #1
# initialisasi variable dan tipe data
a = 0
b = 4.5
c = 'kata'

# contoh output program
print("Kasus 1- Copy Cat #1 (20 Point)")
print(type(a))  # Tipe data integer
print("\t Nilai bilangan bulat a adalah", a, "\n")
print(type(b))  # tipe data float
print("\t Nilai bilangan decimal b adalah", b, "\n")
print(type(c))  # tipe data float
print("\t Kata dari c adalah", c, "\n")


# Kasus 2- Copy Cat #2
# initialisasi Variable dan tipe data
print("Kasus 2- Copy Cat #2 (20 Point)")
umur = 18
berat_badan = 48.3
# Contoh output program dengan variasi print
print("Umur saya", umur, "tahun")
print("Umur saya", umur)
print("Umur saya", str(umur), "tahun")
print("Umur saya %d" % umur)
print("Umur saya %f" % (berat_badan))
print("Berat badan saya {} kilogram".format(berat_badan))
print("\n")


# Kasus 3- Lupa Ortu
print("Kasus 3 - Lupa Ortu (30 Point)")
namaAyah = "Ayah : Jono"
namaIbu = "Ibu : Jeni"
print(namaAyah)
print(namaIbu)
print('\n')


print("Kasus 4- Cek Error (30 Point")
# Kasus 4- Cek Error
# Kamus
a = 1
b = 4

# algoritma
print("Hasil a yang pertama:", a)
print("Hasil b yang pertama:" + str(b))

b = a + 1
a -= b
print("Hasil a yang kedua:"+str(a))
print("Hasil b yang kedua:", b)

a = b + 2
b = a * b
print("Hasil a yang ketiga: {}".format(a))
print("Hasil b yang ketiga: %f" % (b))


c = a
a *= 2
b = c
print("Hasil a yang keempat: {}".format(a))
print("Hasil b yang keempat:{}". format(b))
