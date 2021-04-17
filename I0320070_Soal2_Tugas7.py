numerik = input("Masukan angka (pisahkan dengan spasi): ").split()

for i in range(len(numerik)):
    numerik[i] = int(numerik[i])

rata_rata = sum(numerik)/len(numerik)
print("Rata-rata tinggi badan siswa adalah ", rata_rata)

import math

print("Rata-rata dengan pembulatan ke atas= ", math.ceil(rata_rata))

print("Nilai tertinggi= ", max(numerik))