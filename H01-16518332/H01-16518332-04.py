# NIM/Nama  : 16518332/Dhafin Rayhan Ahmad
# Tanggal   : 8 September 2018
# Deskripsi : Menentukan warna yang muncul dari nilai hue

# KAMUS
# (berdasarkan instruksi dosen)
# h: integer, nilai hue, input dari pengguna
# r: string, teks "Red."
# y: string, teks "Yellow."
# g: string, teks "Green."
# c: string, teks "Cyan."
# b: string, teks "Blue."
# m: string, teks "Magenta."
# x: string, r/y/g/c/b/m akan dimasukkan nilainya pada variabel ini

# Meminta input nilai hue
h = int(input("Masukkan nilai hue: "))

# Teks output warna
r = "Red."
y = "Yellow."
g = "Green."
c = "Cyan."
b = "Blue."
m = "Magenta."

# Variabel warna
x = ""

# Menentukan warna
if h <= 30:
    x = r
elif h <= 90:
    x = y
elif h <= 150:
    x = g
elif h <= 210:
    x = c
elif h <= 270:
    x = b
elif h <= 330:
    x = m
else: # h <=360
    x = r

# Output warna
print("Hue " + str(h) + " merepresentasikan warna " + x)
