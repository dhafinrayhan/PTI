# NIM/Nama  : 16518332/Dhafin Rayhan Ahmad
# Tanggal   : 7 September 2018
# Deskripsi : Mencari waktu sebelum alarm berbunyi dari waktu sekarang

# KAMUS
# (berdasarkan instruksi dosen)
# js: integer, jam pada waktu sekarang, merupakan input dari pengguna
# ms: integer, menit pada waktu sekarang, merupakan input dari pengguna
# ds: integer, detik pada waktu sekarang, merupakan input dari pengguna
# ja: integer, jam pada waktu alarm, merupakan input dari pengguna
# ma: integer, menit pada waktu alarm, merupakan input dari pengguna
# da: integer, detik pada waktu alarm, merupakan input dari pengguna
# ks: integer, hasil konversi waktu sekarang ke dalam detik
# ka: integer, hasil konversi waktu alarm ke dalam detik
# sel: integer, selisih waktu sekarang dengan waktu alarm (dalam detik)
# jsel: integer, jam pada selisih waktu sekarang dengan waktu alarm
# msel: integer, menit pada selisih waktu sekarang dengan waktu alarm
# dsel: integer, detik pada selisih waktu sekarang dengan waktu alarm

# Meminta input waktu sekarang
print("Masukkan waktu sekarang!")
js = int(input("Jam : "))
ms = int(input("Menit : "))
ds = int(input("Detik : "))

# Meminta input waktu alarm
print("Masukkan waktu alarm!")
ja = int(input("Jam : "))
ma = int(input("Menit : "))
da = int(input("Detik : "))

# Konversi waktu ke dalam bentuk detik dalam sehari (0 sampai 86399)
ks = 3600*js + 60*ms + ds # hasil konversi waktu sekarang
ka = 3600*ja + 60*ma + da # hasil konversi waktu alarm

# Jika hasil konversi waktu alarm kurang dari hasil konversi waktu sekarang,
# maka alarm akan bunyi pada hari berikutnya sehingga perlu ditambah 86400 detik
if ka < ks:
    ka += 86400

# Selisih waktu alarm dengan waktu sekarang
sel = ka - ks

# Konversi kembali menjadi jam, menit, dan detik
jsel = sel // 3600 # selisih waktu dalam detik dibagi 3600 dengan floor untuk mendapatkan jam
msel = (sel % 3600) // 60 # sisa dari selisih waktu dalam detik dibagi 60 dengan floor untuk mendapatkan menit
dsel = sel % 60 # sisa dari selisih waktu dalam detik setelah dijadikan jam dan menit

# Output selisih waktu
print("Alarm akan berbunyi dalam " + str(jsel) + " jam " + str(msel) + " menit " + str(dsel) + " detik lagi.")
