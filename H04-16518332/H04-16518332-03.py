# NIM/Nama  : Dhafin Rayhan Ahmad
# Tanggal   : 22 Oktober 2018
# Deskripsi : Analisis data karyawan

import pandas as pd

df = pd.read_csv("stei-b-3.csv")

# SOAL 1
# Banyaknya data
print(len(df))
# 9079

# SOAL 2
# Data karyawan bernama Tuan Yon
print(df.loc[df["nama"] == "Tuan Yon"])
#           nama departemen  tahun_masuk  usia  golongan     gaji
# 2227  Tuan Yon  teknologi         2017    31        10  9939125

# SOAL 3
# Banyaknya karyawan dengan usia kurang dari atau sama dengan 30
print(len(df.loc[df["usia"] <= 30]))
# 1542

# SOAL 4
# Banyaknya karyawan personalia dengan gaji di luar rentang 4 - 5 juta
print(len(df.loc[(df["departemen"] == "personalia") & ((df["gaji"] < 4000000) | (df["gaji"] > 5000000))]))
# 1122

# SOAL 5
# Data karyawan produksi dengan gaji maksimum
df_produksi = df.loc[df["departemen"] == "produksi"] # DataFrame dengan departemen = produksi
df_produksi_max = df_produksi.max()
print(df_produksi.loc[df_produksi["gaji"] == df_produksi_max["gaji"]])
#                  nama departemen  tahun_masuk  usia  golongan     gaji
# 5047  Ario Nuswantoro   produksi         2014    36         3  9995982

# SOAL 6
# Data 10 karyawan teknologi dengan gaji terbanyak. Jika ada gaji yang sama banyak, urutkan dari usia yang termuda
df_teknologi = df.loc[df["departemen"] == "teknologi"] # DataFrame dengan departemen = teknologi
df_teknologi_sort = df_teknologi.sort_values(["gaji", "usia"], ascending=[0,1])
print(df_teknologi_sort[0:10])
#                          nama departemen   ...     golongan     gaji
# 3282   Jawahir Asy Mahdy Maro  teknologi   ...            1  9996959
# 8971         Vania Avviantari  teknologi   ...            1  9994946
# 4972               Brian Luas  teknologi   ...            1  9989154
# 6127       Tiara Fahiramadyan  teknologi   ...            1  9987370
# 6260               Vivi Novia  teknologi   ...            1  9986306
# 3739            Nana Restiana  teknologi   ...            1  9982168
# 8275  Rizkiyani Nadifa Puteri  teknologi   ...            1  9956570
# 3365         Zaki Abdurrasyid  teknologi   ...            1  9951235
# 7410     Made Santihayu Sukma  teknologi   ...            1  9944009
# 8194          Naufal Arifandy  teknologi   ...            1  9941846

# SOAL 7
# Tabel frekuensi banyaknya karyawan tiap golongan
print(df["golongan"].value_counts())
# 9     945
# 6     927
# 5     925
# 2     913
# 8     908
# 7     905
# 1     903
# 3     902
# 4     876
# 10    875
# Name: golongan, dtype: int64

# SOAL 8
# Tabel frekuensi banyaknya karyawan tiap departemen yang masuk sebelum tahun 2015
df_b2015 = df.loc[df["tahun_masuk"] < 2015] # DataFrame dengan tahun < 2015
print(df_b2015["departemen"].value_counts())
# keuangan       546
# marketing      544
# produksi       530
# teknologi      522
# kreatif        501
# personalia     480
# operasional    476
# Name: departemen, dtype: int64

# SOAL 9
# Rata-rata gaji seluruh karyawan
print(df["gaji"].mean())
# 5476321.027756361

# SOAL 10
# Standar deviasi usia karyawan operasional
df_operasional = df.loc[df["departemen"] == "operasional"] # DataFrame dengan departemen = operasional
print(df_operasional["usia"].std())
# 10.436347593016766

# SOAL 11
# Dengan apakah gaji berkorelasi? Usia, tahun masuk, atau golongan? Tuliskan koefisien korelasinya
# Berdasarkan bahasa soal, dapat diketahui bahwa gaji pasti berkorelasi dengan salah satu dari usia/tahun_masuk/golongan
corr_gajiusia = df["gaji"].corr(df["usia"])
corr_gajitahunmasuk = df["gaji"].corr(df["tahun_masuk"])
corr_gajigolongan = df["gaji"].corr(df["golongan"])
# Membuat logic untuk menentukan jawaban soal
if abs(corr_gajiusia) > abs(corr_gajitahunmasuk):
    if abs(corr_gajiusia) > abs(corr_gajigolongan):
        print("usia")
        print(corr_gajiusia)
    else: # abs(corr_gajiusia) < abs(corr_gajigolongan)
        print("golongan")
        print(corr_gajigolongan)
else:
    print("tahun_masuk")
    print(corr_gajitahunmasuk)
# golongan
# -0.8708577012378015
