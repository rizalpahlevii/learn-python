def nilaiAngka(val):
    if val >= 85:
        return ['A', 4]
    elif val <= 84 and val >= 70:
        return ['B', 3]
    elif val <= 69 and val >= 60:
        return ['C', 2]
    elif val <= 59 and val >= 50:
        return ['D', 1]
    else:
        return ['E', 0]


def ipk(arr):
    total = 0
    for i in arr:
        total += nilaiAngka(i)[1]
    return total / len(arr)


def displayTranskrip(nim, name, mataKuliah, nilai):
    print('Nim:', nim)
    print('Nama:', name)
    for i in range(len(mataKuliah)):
        print('Makul', mataKuliah[i], 'Nilai Angka',
              nilai[i], 'Nilai Huruf', nilaiAngka(nilai[i])[0])
    print('IPK:', ipk(nilai))
    print('Cumclaude') if ipk(nilai) >= 3.5 else print('Tidak Cumclaude')
