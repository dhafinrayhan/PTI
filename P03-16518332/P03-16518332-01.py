# NIM/Nama	: 16518332/Dhafin Rayhan Ahmad
# Tanggal	: 3 Oktober 2018
# Deskripsi	: Mentranslasi suatu bilangan heksadesimal 1 digit ke bilangan desimal

# FUNGSI
def HtoD(x): # fungsi yang akan mengembalikan nilai translasi suatu bilangan heksadesimal 1 digit (x) ke bilangan desimal
	if x == "A":
		return 10
	elif x == "B":
		return 11
	elif x == "C":
		return 12
	elif x == "D":
		return 13
	elif x == "E":
		return 14
	elif x == "F":
		return 15
	else: # jika x adalah "0"-"9"
		return int(x) # nilainya sama
		
# INPUT
h = input("Masukkan karakter heksadesimal: ")

# OUTPUT
print("Representasi desimalnya " + str(HtoD(h)))
