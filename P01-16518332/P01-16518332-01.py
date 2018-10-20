# NIM/Nama	: 16518332/Dhafin Rayhan Ahmad
# Tanggal	: 5 September 2018
# Deskripsi	: Tuan Yon mencari kuadran dari suatu titik

x = int(input("Masukkan nilai x: ")) # minta nilai x
y = int(input("Masukkan nilai y: ")) # minta nilai y

kuadran = 0 # kuadran sementara, untuk kasus x != 0 dan y !=0

if x == 0: 
	if y == 0:
		print("(0,0) ada di titik pusat.")
	else:
		print("(0,"+str(y)+") ada di sumbu y.")
		
elif y == 0:
	print("("+str(x)+",0) ada di sumbu x.")
	
else:
	if x > 0:
		if y > 0:
			kuadran = 1
		else:
			kuadran = 4
			
	else:
		if y > 0:
			kuadran = 2
		else:
			kuadran = 3
			
	print("("+str(x)+","+str(y)+") ada di kuadran "+str(kuadran)+".")
