# NIM/Nama	: 16518332/Dhafin Rayhan Ahmad
# Tanggal	: 3 Oktober 2018
# Deskripsi	: Menjumlahkan dua bilangan heksadesimal 2 digit

# FUNGSI
def HtoD1(x): # fungsi yang akan mengembalikan nilai translasi suatu bilangan heksadesimal 1 digit (x) ke bilangan desimal
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
		
def HtoD2(a,b): # fungsi yang akan mengembalikan nilai translasi suatu bilangan heksadesimal 2 digit (ab) ke bilangan desimal
	c = 16 * HtoD1(a) # ubah digit pertama heksadesimal ke dalam desimal
	d = HtoD1(b) # ubah digit kedua heksadesimal ke dalam desimal
	return c+d # hasilnya dalam bentuk desimal
	
def DtoH1(x): # fungsi yang akan mengembalikan nilai translasi suatu bilangan desimal digit (x) ke bilangan heksadesimal 1 digit
	if x == 10:
		return "A"
	elif x == 11:
		return "B"
	elif x == 12:
		return "C"
	elif x == 13:
		return "D"
	elif x == 14:
		return "E"
	elif x == 15:
		return "F"
	else: # jika x adalah 0-9
		return str(x) # nilainya sama
		
def DtoH2(x): # fungsi yang akan mengembalikan nilai translasi suatu bilangan desimal digit (x) ke bilangan heksadesimal 2 digit
	c = DtoH1(x//16) # digit pertama bilangan heksadesimal, dengan memanfaatkan pembagian floor 16
	d = DtoH1(x%16) # digit pertama bilangan heksadesimal, dengan memanfaatkan modulo 16
	return c+d # hasilnya dalam bentuk heksadesimal
	
# INPUT
A1 = input("Masukkan digit pertama bilangan A: ")
A2 = input("Masukkan digit kedua bilangan A: ")
B1 = input("Masukkan digit pertama bilangan B: ")
B2 = input("Masukkan digit kedua bilangan B: ")

# PROSES
hasil = DtoH2(HtoD2(A1,A2) + HtoD2(B1,B2)) # input diubah menjadi desimal, kemudian dijumlahkan, lalu diubah menjadi heksadesimal

# OUTPUT
print(A1+A2 +" + "+ B1+B2 +" = "+ hasil)
