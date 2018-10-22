# NIM/Nama  : Dhafin Rayhan Ahmad
# Tanggal   : 22 Oktober 2018
# Deskripsi : Analisis data nilai mahasiswa

import pandas as pd

df = pd.read_csv("stei-b-1.csv")

# SOAL 1
# Banyaknya data
print(len(df))
# 9628

# SOAL 2
# Nilai matematika, fisika, dan kimia dari mahasiswa bernama Tuan Yon.
data_Tuan_Yon = (df["nama"] == "Tuan Yon") # mencari data Tuan Yon
print(df.loc[data_Tuan_Yon, "nilai_mat"]) # mengambil nilai matematika
print(df.loc[data_Tuan_Yon, "nilai_fis"]) # mengambil nilai fisika
print(df.loc[data_Tuan_Yon, "nilai_kim"]) # mengambil nilai kimia
# 8404    91
# Name: nilai_mat, dtype: int64
# 8404    83
# Name: nilai_fis, dtype: int64
# 8404    63
# Name: nilai_kim, dtype: int64

# SOAL 3
# Banyaknya mahasiswa dengan nilai matematika di atas 80
print(len(df.loc[df["nilai_mat"] > 80]))
# 2789

# SOAL 4
# Banyaknya mahasiswa yang mendapat nilai kurang dari 40 di matkul apapun
print(len(df.loc[(df["nilai_mat"] < 40) | (df["nilai_fis"] < 40) | (df["nilai_kim"] < 40)]))
# 4351

# SOAL 5
# Banyaknya mahasiswa yang mendapat nilai terendah di fisika
dfmin = df.min()
print(len(df.loc[df["nilai_fis"] == dfmin["nilai_fis"]])) # menentukan minimum dari nilai_fis terlebih dahulu
# 126

# SOAL 6
# Data 10 besar peserta peraih nilai tertinggi di fisika. Jika ada yang nilainya sama, ambil mahasiswa dengan nama lebih kecil
df_sort = df.sort_values(["nilai_fis", "nama"], ascending=[0, 1]) # DataFrame yang sudah terurut sesuai ketentuan
print(df_sort[0:10])
#                         nama fakultas    ...      nilai_fis  nilai_kim
# 1905           Abdillah Aziz     FTMD    ...             99         23
# 3489  Agatha Nabilla Lestari     STEI    ...             99         81
# 5087    Ahmad Zahi Ulul Azmi     FTMD    ...             99         81
# 2822          Aidah Fithriah     FTMD    ...             99         81
# 1431                  Albert     FTMD    ...             99         25
# 5317        Alexander Sukono     FTMD    ...             99         81
# 6169            Alfred Andry     STEI    ...             99         81
# 7403    Alief Rizky Ramadhan    SITHR    ...             99         81
# 3046   Alwidya Angga Safitri     FTSL    ...             99         81
# 7060  Alyssa Nadhira Windari     FTMD    ...             99         81
# 
# [10 rows x 5 columns]

# SOAL 7
# Tabel frekuensi masing-masing fakultas
print(df["fakultas"].value_counts())
# FTSL     2475
# STEI     2416
# SITHR    2376
# FTMD     2361
# Name: fakultas, dtype: int64

# SOAL 8
# Rata-rata dari nilai matematika semua mahasiswa
print(df["nilai_mat"].mean())
# 65.24293726630661

# SOAL 9
# Standar deviasi dari nilai fisika semua mahasiswa
print(df["nilai_fis"].std())
# 25.7295023400875

# SOAL 10
# Rata-rata dari nilai kimia STEI
df_stei = df.loc[df["fakultas"] == "STEI"] # DataFrame dengan fakultas = STEI
print(df_stei["nilai_kim"].mean())
# 50.226407284768214

# SOAL 11
# Dengan nilai manakah (matematika / kimia) nilai fisika berkorelasi? Berapa koefisien korelasinya?
# Berdasarkan bahasa soal, dapat diketahui bahwa nilai fisika pasti berkorelasi dengan salah satu dari nilai matematika/kimia
corr_fismat = df["nilai_fis"].corr(df["nilai_mat"])
corr_fiskim = df["nilai_fis"].corr(df["nilai_kim"])
# Membuat logic untuk menentukan jawaban soal
if abs(corr_fismat) > abs(corr_fiskim):
    print("nilai_mat")
    print(corr_fismat)
else: # abs(corr_fismat) < abs(corr_fiskim)
    print("nilai_kim")
    print(corr_fiskim)
# nilai_kim
# 0.8246142287210514
