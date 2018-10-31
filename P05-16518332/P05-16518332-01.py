# NIM/Nama	: Dhafin Rayhan Ahmad
# Tanggal	: 31 Oktober 2018
# Deskripsi	: Analisis dan visualisasi data IP mahasiswa

import matplotlib
import pandas as pd
matplotlib.use("agg")
import matplotlib.pyplot as plt

df = pd.read_csv("stei-b.csv")
# 1. Banyaknya data
print(len(df))
# 9061

# 2. Pie chart banyaknya mahasiswa tiap fakultas.
df2 = df["fakultas"].value_counts()
df2.plot(kind="pie")
plt.show()

# 3. Pie chart banyaknya mahasiswa FTSL berdasarkan tingkat
df3 = df.loc[df["fakultas"]=="FTSL"]["tingkat"].value_counts()
df3.plot(kind="pie")
plt.show()

# 4. Histogram dengan IP sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y, gunakan pertambahan 0.5
df[["ip"]].plot(kind="hist",bins=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0])
plt.show()

# 5. Berdasar plot sebelumnya, range ip mana yang paling banyak diperoleh?

# Range IP yang paling banyak diperoleh adalah 3.0-3.5.

# 6. Stacked bar chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa tiap fakultas sebagai stacked sumbu y
df6 = df.groupby(["tingkat","fakultas"])["nama"].size().unstack()
df6.plot(kind="bar",stacked=True)
plt.show()

# 7. Berdasar plot sebelumnya, angkatan ke berapa STEI jumlah mahasiswanya paling sedikit?

# Jumlah mahasiswa STEI paling sedikit pada angkatan 2018.

# 8. Line chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y
df8 = df["tingkat"].value_counts()
df8.plot(kind="line",x="tingkat",y=[df8])
plt.show()

# 9. Line chart seperti soal sebelumnya, namun terdapat 4 garis, masing-masing untuk tiap fakultas.
df.plot(kind="line",x="tingkat",y=["fakultas",df8])
plt.show()

# 10. Berdasar plot sebelumnya, fakultas manakah yang jumlah mahasiswanya terus bertambah?

# SITHR

# 11. Berdasar plot sebelumnya, fakultas manakah yang jumlah mahasiswanya terus berkurang?

# STEI

