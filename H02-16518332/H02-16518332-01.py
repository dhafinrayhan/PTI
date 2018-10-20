# NIM/Nama  : 16518332/Dhafin Rayhan Ahmad
# Tanggal   : 22 September 2018
# Deskripsi : Menentukan jumlah anggota tim dengan FPB

# Input
f = int(input("Masukkan jumlah fakultas: "))

m = [0 for i in range(f)] # list jumlah mahasiswa tiap fakultas
maks = 0 # maksimal mahasiswa dalam satu fakultas (sementara) (sebenarnya hanya butuh minimal)
for i in range(f): # meminta input jumlah mahasiswa tiap fakultas
    m[i] = int(input("Jumlah mahasiswa dari fakultas " + str(i+1) + ": "))
    if m[i] > maks: # jika mendapatkan maks baru
        maks = m[i]
        
# Pencarian FPB
fpb = 0 # fpb sementara (pencarian sebenarnya akan dimulai dari 1)

for i in range(maks): # coba-coba pembagi dari 1 sampai maks (sebenarnya bisa sampai min. saja)
    hitung = 0 # ada berapa fakultas yang bisa dibagi i+1

    for j in range(f):
        if m[j]%(i+1) == 0: # jika jumlah mahasiswa fakultas j+1 bisa dibagi i+1
            hitung += 1

    if hitung == f: # jika semua fakultas bisa dibagi i+1
        fpb = i+1 # maka i+1 menjadi fpb sementara

# Output
print("Jumlah anggota tim terbanyak yang mungkin adalah " + str(fpb))
