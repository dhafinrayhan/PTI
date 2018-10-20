# NIM/Nama  : 16518332/Dhafin Rayhan Ahmad
# Tanggal   : 22 September 2018
# Deskripsi : Membuat segitiga dari 3 lidi

# Input
y = int(input("Masukkan banyaknya stik Tuan Yon: "))
print("Masukkan panjang stik Tuan Yon:")
sy = [0 for i in range(y)] # list panjang stik-stik Tuan Yon
for i in range(y):
    sy[i] = int(input()) # input panjang stik ke-(i+1) milik Tuan Yon

r = int(input("Masukkan banyaknya stik Nyai Rin: "))
print("Masukkan panjang stik Nyai Rin:")
sr = [0 for i in range(r)] # list panjang stik-stik Nyai Rin
for i in range(r):
    sr[i] = int(input()) # input panjang stik ke-(i+1) milik Nyai Rin

m = int(input("Masukkan banyaknya stik Tuan Mi: "))
print("Masukkan panjang stik Tuan Mi:")
sm = [0 for i in range(m)] # list panjang stik-stik Tuan Mi
for i in range(m):
    sm[i] = int(input()) # input panjang stik ke-(i+1) milik Tuan Mi

# Output
print("Daftar segitiga yang dapat dibuat:")

# Mencari segitiga yang dapat dibuat
for i in range(y):
    for j in range(r):
        for k in range(m):
            if sy[i] + sr[j] > sm[k] and sr[j] + sm[k] > sy[i] and sm[k] + sy[i] > sr[j]:
                print(str(sy[i]) + " " + str(sr[j]) + " " + str(sm[k])) # output stik-stik yang bisa dibuat segitiga
