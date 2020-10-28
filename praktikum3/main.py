print("Kasus 1 - Cek Error(20 Point)")

# kamus
a = 1
b = 4

# algoritma
print("Hasil a yang pertama:"+str(a))
print("Hasil b yang pertama:"+str(b))

b = a
a -= b
print("Hasil a yang kedua:"+str(a))
print("Hasil b yang kedua:"+str(b))

a = b + 1
b = a / b
print("Hasil a yang ketiga:"+str(a))
print("Hasil b yang ketiga:"+str(b))
print("\n")

print("Kasus 2- Artimatika #1 (25 Point)")
# 2x + y*5
x = 0
y = 1
result = 2 * x + y * 5
print(result)
print("\n")


print("Kasus 3- Artimatika #2 (25 Point)")
# 0.5 * a * t
a = 1.0
t = 3.0
result = 0.5 * a * t
print(result)
print('\n')


print("Kasus 4- Kebut-kebutan! (30 Point)")
vt = 21.55
vo = 0
t = 12.5

a = (vt - vo) / t
print(a)
