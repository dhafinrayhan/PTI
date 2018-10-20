# NIM/Nama	: 16518332/Dhafin Rayhan Ahmad
# Tanggal	: 5 September 2018
# Deskripsi	: Tuan Yon ingin mengetahui siapa yang lebih hebat, Jawa Tengah atau Jawa Barat

gt = int(input("Masukkan perolehan emas Jawa Tengah: ")) # gold J. Tengah
st = int(input("Masukkan perolehan perak Jawa Tengah: ")) # silver J. Tengah
bt = int(input("Masukkan perolehan perak Jawa Tengah: ")) # bronze J. Tengah

gb = int(input("Masukkan perolehan emas Jawa Barat: ")) # gold J. Barat
sb = int(input("Masukkan perolehan perak Jawa Barat: ")) # silver J. Barat
bb = int(input("Masukkan perolehan perak Jawa Barat: ")) # bronze J. Barat

skort = 3*gt + 2*st + 1*bt # skor J. Tengah
skorb = 3*gb + 2*sb + 1*bb # skor J. Barat

def pw(x): # agar tidak banyak mengetik
	if x == 1:
		print("Pemenangnya adalah Jawa Tengah.")
	elif x == 2:
		print("Pemenangnya adalah Jawa Barat.")
	else:
		print("Jawa Tengah dan Jawa Barat masih imbang.")

if skort == skorb: # awal cek berdasarkan skor
	if gt == gb: # awal cek berdasarkan emas
		if st == sb: # awal cek berdasarkan perak
			if bt == bb: # awal cek berdasarkan perunggu
				pw(0)
			elif bt > bb: # sebenarnya tidak mungkin, karena sudah pasti jika skor, emas, dan perak sama, maka perunggu otomatis sama
				pw(1)
			else: # akhir cek berdasarkan perunggu
				pw(2)
		elif st > sb:
			pw(1)
		else: # akhir cek berdasarkan perak
			pw(2)
	elif gt > gb:
		pw(1)
	else: # akhir cek berdasarkan emas
		pw(2)
elif skort > skorb:
	pw(1)
else: # akhir cek berdasarkan skor
	pw(2)
