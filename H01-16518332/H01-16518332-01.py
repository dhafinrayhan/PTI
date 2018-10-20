# NIM/Nama  : 16518332/Dhafin Rayhan Ahmad
# Tanggal   : 7 September 2018
# Deskripsi : Penghitung pesanan pelanggan warung indomie

# KAMUS
# (berdasarkan instruksi dosen)
# f: string, opsi makanan yang dipilih pengguna
# d: string, opsi minuman yang dipilih pengguna
# pf: integer, harga makanan yang dipilih pengguna
# pd: integer, harga minuman yang dipilih pengguna
# pt: integer, total harga yang harus dibayarkan sesuai pilihan pengguna

# Daftar menu makanan
print("Menu makanan:")
print("1. Indomie Single")
print("2. Indomie Double")
print("3. Indomie Telor")

# Meminta input nomor menu makanan
f = input("Masukkan nomor menu makanan: ")

# Daftar menu minuman
print("Menu minuman:")
print("1. Air Putih")
print("2. Teh Manis")
print("3. Kopi")

# Meminta input nomor menu minuman
d = input("Masukkan nomor menu minuman: ")

# Menghitung harga makanan
pf = 0

if f == "1":
    pf = 4000
elif f == "2":
    pf = 8000
elif f == "3":
    pf = 7000

# Menghitung harga minuman
pd = 0

if d == "1":
    pd = 0
elif d == "2":
    pd = 2000
elif d == "3":
    pd = 4000

# Total biaya
pt = pf + pd

# Output biaya
print("Biaya yang harus dibayarkan: " + str(pt))
