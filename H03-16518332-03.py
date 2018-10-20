# NIM/Nama	: 16518332/Dhafin Rayhan Ahmad
# Tanggal	: 6 Oktober 2018
# Deskripsi	: Menentukan KPK dari tiga bilangan

# FUNGSI
def FPB(a,b): # menentukan FPB dari dua bilangan
    batas = a # batas pencarian FPB
    if b>a:
        batas = b # maka b menjadi batas pencarian

    fpb = 1 # FPB sementara
    for i in range(1,batas+1): # mencari FPB
        if (a%i==0) and (b%i==0): # jika a dan b keduanya habis dibagi i
            fpb = i # maka i menjadi fpb sementara

    return fpb # kembalikan nilai fpb

def KPK(a,b): # menentukan KPK dari dua bilangan
    return int((a*b)/(FPB(a,b))) # menggunakan rumus yang diberikan

def KPK3(a,b,c): # menentukan KPK dari tiga bilangan
    return KPK(a,KPK(b,c)) # menggunakan definisi yang diberikan

# INPUT
A = int(input("Masukkan bilangan A: "))
B = int(input("Masukkan bilangan B: "))
C = int(input("Masukkan bilangan C: "))

# OUTPUT
print("KPK dari " + str(A) + ", " + str(B) + ", dan " + str(C) + " adalah " + str(KPK3(A,B,C)) + ".")
