# NIM/Nama	: 16518332/Dhafin Rayhan Ahmad
# Tanggal	: 6 Oktober 2018
# Deskripsi	: Menentukan pasangan-pasangan bilangan komposit

# FUNGSI
def Komp(x): # memeriksa apakah sebuah bilangan komposit
    faktor = 0 # banyaknya faktor dari x (sementara)

    for i in range(1,x+1): # mencari banyaknya faktor dari x
        if x%i == 0: # jika x habis dibagi i
            faktor += 1 # banyaknya faktor ditambah 1

    if faktor <= 2: # tentu bukan komposit
        return False
    else: # faktor > 2
        return True

def KompKomp(a,b): # memeriksa apakah dua bilangan merupakan pasangan bilangan komposit
    # a harus komposit, b harus komposit, dan (a+b) harus komposit (ketiganya harus terpenuhi)
    return Komp(a) and Komp(b) and Komp(a+b)

# INPUT
A = int(input("Masukkan A: "))
B = int(input("Masukkan B: "))

# PROSES DAN OUTPUT
print("Pasangan bilangan komposit:")

# Memeriksa pasangan-pasangan bilangan komposit dari A (inklusif) hingga B (inklusif)
for i in range(A,B+1): # loop untuk bil. pertama (kiri)
    for j in range(i+1,B+1): # loop untuk bil. kedua (kanan) - bil. kiri & bil. kanan tidak boleh sama
        if KompKomp(i,j): # jika pasangan bilangan komposit
            print(str(i) + " " + str(j))
