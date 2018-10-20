# NIM/Nama	: 16518332/Dhafin Rayhan Ahmad
# Tanggal	: 19 September 2018
# Deskripsi	: Menuliskan bilangan-bilangan prima yang ada dari A hingga B

# Input
A = int(input("Masukkan A: "))
B = int(input("Masukkan B: "))

# Output bag. 1
print("Bilangan prima dari A hingga B: ")

# Mencari bilangan prima dari A hingga B
for i in range(A,B+1): # Tes untuk bilangan dari A hingga B, apakah bilangan tersebut prima
	pembagi = 0 # bilangan bulat yang bisa membagi i. Jika 2, maka bilangan i prima
	for j in range(i): # mencari berapa banyak pembagi bilangan i
		if i%(j+1) == 0: # jika i habis dibagi j+1 (berarti j+1 membagi i)
			pembagi += 1
	
	# Output bag. 2		
	if pembagi == 2: # jika pembagi i ada 2, maka i prima
		print(i)
