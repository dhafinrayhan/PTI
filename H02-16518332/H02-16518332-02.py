# NIM/Nama  : 16518332/Dhafin Rayhan Ahmad
# Tanggal   : 22 September 2018
# Deskripsi : Mengalikan dua polinom

# Input
df = int(input("Masukan derajat f: "))

kf = [0 for i in range(df+1)] # list koefisien-koefisien dalam f
for i in range(df+1): # meminta input untuk tiap koefisien
    kf[df-i] = int(input("Masukan koefisien x^" + str(df-i) + ": "))

dg = int(input("Masukan derajat g: "))

kg = [0 for i in range(dg+1)] # list koefisien-koefisien dalam g
for i in range(dg+1): # meminta input untuk tiap koefisien
    kg[dg-i] = int(input("Masukan koefisien x^" + str(dg-i) + ": "))

# Mencari hasil perkalian
kh = [0 for i in range(df+dg+1)] # list koefisien pada polinom hasil

for i in range(df+1):
    for j in range(dg+1):
        kh[i+j] += kf[i]*kg[j] # (koefisien x^i pada f) dikali (koefisien x^j pada g) nilainya ditambahkan pada koefisien x^(i+j) pada polinom hasil

# Output
print("Hasil perkalian polinom:")

for i in range(df+dg+1): # memeriksa tiap koefisien pada polinom hasil
    if i == 0: # untuk pangkat terbesar (yang paling depan)
        if kh[df+dg-i] < 0: # jika koefisien negatif
            print("- " + str(-kh[df+dg-i]) + "x^" + str(df+dg-i), end="") # contoh: "- 5x^3"
        else: # jika koefisien nol atau positif
            print(str(kh[df+dg-i]) + "x^" + str(df+dg-i), end="") # contoh: "5x^3"
    else: # jika bukan yang paling depan
        if kh[df+dg-i] < 0: # jika koefisien negatif
            print(" - " + str(-kh[df+dg-i]) + "x^" + str(df+dg-i), end="") # contoh: " - 5x^3"
        else: # jika koefisien nol atau positif
            print(" + " + str(kh[df+dg-i]) + "x^" + str(df+dg-i), end="") # contoh: " + 5x^3"
