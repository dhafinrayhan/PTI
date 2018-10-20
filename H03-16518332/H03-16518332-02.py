# NIM/Nama	: 16518332/Dhafin Rayhan Ahmad
# Tanggal	: 6 Oktober 2018
# Deskripsi	: Menentukan pasangan-pasangan bilangan prima

# FUNGSI
def Prima(x): # memeriksa apakah sebuah bilangan prima
    faktor = 0 # banyaknya faktor dari x (sementara)

    for i in range(1,x+1): # mencari banyaknya faktor dari x
        if x%i == 0: # jika x habis dibagi i
            faktor += 1 # banyaknya faktor ditambah 1

    if faktor == 2: # maka bilangan prima
        return True
    else: # faktor != 2
        return False

def PrimaPrima(a,b): # memeriksa apakah dua bilangan merupakan pasangan bilangan prima
    # a harus prima, b harus prima, dan ab (bil. a disambung bil. b) harus prima (ketiganya harus terpenuhi)
    return Prima(a) and Prima(b) and Prima(int(str(a)+str(b))) # str(a)+str(b) untuk menyambung a dan b, int(...) untuk mengubah menjadi integer kembali

# INPUT
A = int(input("Masukkan A: "))
B = int(input("Masukkan B: "))

# PROSES DAN OUTPUT
print("Pasangan bilangan prima:")

# Memeriksa pasangan-pasangan bilangan prima dari A (inklusif) hingga B (inklusif)
for i in range(A,B+1): # loop untuk bil. pertama (kiri)
    for j in range(A,B+1): # loop untuk bil. kedua (kanan) - jika bil. kiri & bil. kanan sama maka tidak mungkin termasuk karena bisa dibagi (10*(panjang bil.)+1)
        if PrimaPrima(i,j): # jika pasangan bilangan prima
            print(str(i) + " " + str(j))
