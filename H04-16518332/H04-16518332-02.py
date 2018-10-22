# NIM/Nama  : Dhafin Rayhan Ahmad
# Tanggal   : 22 Oktober 2018
# Deskripsi : Analisis data penerbangan

import pandas as pd

df = pd.read_csv("stei-b-2.csv")

# SOAL 1
# Banyaknya data
print(len(df))
# 7948

# SOAL 2
# Data penerbangan yang memiliki harga 1.999.999
print(df.loc[df["harga"] == 1999999])
#       maskapai asal tujuan  tahun  penumpang    harga
# 3411  rajawali  SRG    BDO   2017        101  1999999

# SOAL 3
# Banyaknya penerbangan dengan harga di atas 3.500.000
print(len(df.loc[df["harga"] > 3500000]))
# 1255

# SOAL 4
# Banyaknya penerbangan di tahun 2014 dengan asal atau tujuan bukan kota PDG
print(len(df.loc[(df["tahun"] == 2014) & (df["asal"] != "PDG") & (df["tujuan"] != "PDG")]))
# 1700

# SOAL 5
# Data penerbangan maskapai macan dengan harga minimum
df_macan = df.loc[df["maskapai"] == "macan"] # DataFrame dengan maskapai = macan
df_macan_minharga_id = df_macan["harga"].idxmin() # index harga terendah pada df_macan
print(df_macan.loc[df_macan_minharga_id])
# maskapai       macan
# asal             JOG
# tujuan           BTH
# tahun           2014
# penumpang         60
# harga        1000420
# Name: 6060, dtype: object

# SOAL 6
# Data 10 penerbangan rajawali dengan penumpang terbanyak. Jika ada penerbangan yang sama banyak, urutkan berdasar harga dari yang termurah
df_rajawali = df.loc[df["maskapai"] == "rajawali"] # DataFrame dengan maskapai = rajawali
df_rajawali_sort = df.sort_values(["penumpang", "harga"], ascending=[0, 1])
print(df_rajawali_sort[0:10])
#           maskapai asal tujuan  tahun  penumpang    harga
# 1629    water asia  JOG    DPS   2016        200  2321680
# 708     water asia  BDO    UPG   2014        200  3972916
# 7542      rajawali  JOG    HLP   2015        200  3973270
# 3620    water asia  JOG    SRG   2016        200  3973482
# 7671         macan  PKU    UPG   2015        200  3973916
# 5711      rajawali  PKU    UPG   2017        200  3974025
# 5849    water asia  KNO    HLP   2014        200  3975250
# 4414      rajawali  CGK    BTH   2017        200  3975674
# 5111    water asia  JOG    PDG   2015        200  3976134
# 3960  country link  BDO    PDG   2017        200  3976905

# SOAL 7
# Tabel frekuensi penerbangan country link masing-masing tahun
df_countrylink = df.loc[df["maskapai"] == "country link"] # DataFrame dengan maskapai = country link
print(df_countrylink["tahun"].value_counts())
# 2017    437
# 2014    414
# 2015    374
# 2016    366
# Name: tahun, dtype: int64

# SOAL 8
# Rata-rata harga seluruh penerbangan
print(df["harga"].mean())
# 2491494.6465777555

# SOAL 9
# Standar deviasi jumlah penumpang maskapai mataram
df_mataram = df.loc[df["maskapai"] == "mataram"] # DataFrame dengan maskapai = mataram
print(df_mataram["penumpang"].std())
# 41.266006289202664

# SOAL 10
# Rata-rata dari harga maskapai country link
# df_countrylink sudah dibuat pada SOAL 7
print(df_countrylink["harga"].mean())
# 2503205.1458202386

# SOAL 11
# Koefisien korelasi dari jumlah penumpang dengan harga
print(df["penumpang"].corr(df["harga"]))
# 0.9745972176473993
