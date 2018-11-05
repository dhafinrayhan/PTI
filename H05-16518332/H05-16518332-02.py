# NIM/Nama  : 16518332/Dhafin Rayhan Ahmad
# Tanggal   : 5 November 2018
# Deskripsi : Analisis dan visualisasi data kesehatan mahasiswa

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stei-b-2.csv")

# SOAL 1
# Banyaknya data
print(len(df))
# 9023

# SOAL 2
# Pie chart banyaknya mahasiswa tiap gender.
df2 = df["gender"].value_counts()
df2.plot(kind="pie")
plt.show()

# SOAL 3
# Berdasarkan plot sebelumnya, gender mana yang lebih mayoritas?

# Gender M merupakan mayoritas.

# SOAL 4
# Bar chart dengan fakultas sebagai sumbu x dan jumlah mahasiswa dengan tinggi di atas 160 sebagai sumbu y.
df4 = df.loc[df["tinggi"]>160].groupby("fakultas")["nama"].size()
df4.plot(kind="bar")
plt.show()

# SOAL 5
# Histogram dengan tinggi sebagai sumbu x dan jumlah mahasiswa laki-laki sebagai sumbu y.
df5 = df.loc[df["gender"]=="M"]
df5[["tinggi"]].plot(kind="hist")
plt.show()

# SOAL 6
# Stacked bar chart dengan fakultas sebagai sumbu x dan jumlah mahasiswa tiap gender sebagai stacked sumbu y.
df6 = df.groupby(["fakultas","gender"])["nama"].size().unstack()
df6.plot(kind="bar",stacked=True)
plt.show()

# SOAL 7
# Berdasar plot sebelumnya, fakultas mana yang rasio mahasiswa perempuannya paling banyak dibanding fakultas lain?

# Rasio mahasiswa perempuan paling banyak pada SITH-R.

# SOAL 8
# Line chart dengan berat badan sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y.
df8 = df.groupby("berat")["nama"].size()
df8.plot(kind="line")
plt.show()

# SOAL 9
# Line chart seperti soal sebelumnya, namun terdapat 2 garis, masing-masing untuk tiap gender.
df9 = df.groupby(["berat","gender"])["nama"].size().unstack()
df9.plot(kind="line")
plt.show()

# SOAL 10
# Berdasar plot sebelumnya, gender manakah yang cenderung memiliki berat lebih ringan?

# Gender F cenderung memiliki berat badan lebih ringan.

# SOAL 11
# Scatter plot dengan berat badan sebagai sumbu x dan tinggi badan sebagai sumbu y
df.plot(kind="scatter",x="berat",y="tinggi")
plt.show()
