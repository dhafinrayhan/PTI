# NIM/Nama  : 16518332/Dhafin Rayhan Ahmad
# Tanggal   : 5 November 2018
# Deskripsi : Analisis dan visualisasi data kendaraan mahasiswa

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stei-b-1.csv")

# SOAL 1
# Banyaknya data
print(len(df))
# 9312

# SOAL 2
#  Pie chart banyaknya mahasiswa tiap kendaraan yang digunakan untuk berangkat ke kampus.
df2 = df["kendaraan"].value_counts()
df2.plot(kind="pie")
plt.show()

# SOAL 3
# Pie chart banyaknya mahasiswa tiap tingkat yang berjalan kaki
df3 = df.loc[df["kendaraan"]=="jalan kaki"]["tingkat"].value_counts()
df3.plot(kind="pie")
plt.show()

# SOAL 4
# Histogram dengan tingkat sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y
df[["tingkat"]].plot(kind="hist")
plt.show()

# SOAL 5
# Berdasar plot sebelumnya, angkatan berapa yang jumlah mahasiswanya paling banyak?

# Jumlah mahasiswa terbanyak terdapat pada angkatan 2016.

# SOAL 6
# Stacked bar chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa tiap kendaraan sebagai stacked sumbu y
df6 = df.groupby(["tingkat","kendaraan"])["nama"].size().unstack()
df6.plot(kind="bar",stacked=True)
plt.show()

# SOAL 7

# Berdasar plot sebelumnya, sebutkan trend kendaraan transportasi tiap tingkat!
# Motor paling banyak digunakan oleh mahasiswa angkatan 2015.
# Motor paling banyak digunakan oleh mahasiswa angkatan 2016.
# Angkot paling banyak digunakan oleh mahasiswa angkatan 2017.
# Jalan kaki paling banyak digunakan oleh mahasiswa angkatan 2018.

# SOAL 8
# Line chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y
df8 = df.groupby("tingkat")["nama"].size()
df8.plot(kind="line")
plt.show()

# SOAL 9
# Line chart seperti soal sebelumnya, namun terdapat 4 garis, masing-masing untuk tiap kendaraan
df9 = df.groupby(["tingkat","kendaraan"])["nama"].size().unstack()
df9.plot(kind="line")
plt.show()

# SOAL 10
# Berdasar plot sebelumnya, apa kendaraan yang penggemarnya terus bertambah?

# Penggemar angkot terus bertambah tiap angkatan.

# SOAL 11
# Berdasar plot sebelumnya, apa kendaraan yang penggemarnya terus menurun?

# Penggemar motor terus menurun tiap angkatan.
