# NIM/Nama	: 16518332/Dhafin Rayhan Ahmad
# Tanggal	: 19 September 2018
# Deskripsi	: Menjodohkan laki-laki dan perempuan berdasarkan tingkat kegantengan dan kecantikan

# Meminta input data laki-laki
N = int(input("Masukkan jumlah laki-laki: ")) # banyaknya laki-laki
G = [0 for i in range(N)] # declare array tingkat kegantengan
for i in range(N): # input kegantengan
	G[i] = int(input("Masukkan tingkat kegantengan " + str(i+1) + ": ")) # input kegantengan laki-laki ke-(i+1)

# Meminta input data perempuan
M = int(input("Masukkan jumlah perempuan: ")) # banyaknya perempuan
C = [0 for i in range(M)] # declare array tingkat kecantikan
for i in range(M): # input kecantikan
	C[i] = int(input("Masukkan tingkat kecantikan " + str(i+1) + ": ")) # input kecantikan perempuan ke-(i+1)

# Input tolak ukur jodoh (X)
X = int(input("Masukkan nilai X: "))

pasangan = 0 # pasangan jodoh yang ditemukan sementara 0 (belum dicari)

# Cek jodoh
for i in range(N): # Mengecek apakah laki-laki ke-(i+1) memiliki jodoh
	for j in range(M): # Mengecek apakah perempuan ke-(j+1) adalah jodoh dari laki-laki ke-(i+1)
		if G[i] + C[j] == X: # jika memenuhi syarat jodoh
			pasangan += 1 # ditemukan pasangan jodoh, sehingga jumlah pasangan sementara ditambah satu
			
# Output
print("Jumlah pasangan yang jodoh ada " + str(pasangan) + ".")
