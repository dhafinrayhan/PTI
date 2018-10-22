import pandas as pd
df = pd.read_csv("flights.csv")

# LATIHAN-1

# Ambil data pada baris ke-100 s.d. 500
df[99:500]
# Ambil data pada baris ke-100 s.d. 150 pada kolom "origin" dan "dest"
df.loc[99:150,["origin","dest"]]
# Ambil data pada baris ke-100 s.d. 150 pada kolom 3 (dep_time), 5 (arr_time), 7 (carrier)
df.iloc[:,[3,5,7]]
# Dapatkan semua data penerbangan dengan dest = “LAX” untuk carrier = "UA" pada month=6
df.loc[(df["dest"] == "LAX") & (df["carrier"] == "UA") & (df["month"] == 6)]
# Dapatkan data penerbangan dengan distance > 4900
df.loc[df["distance"] > 4900]

# LATIHAN-2

minimum,maximum = (df.min(),df.max()) # mendapatkan nilai minimum & maximum untuk seluruh data

# Tampilkan nilai tertinggi dan terendah untuk air_time
print(maximum["air_time"])
print(minimum["air_time"])
# Tampilkan data penerbangan dengan dep_delay tertinggi
print(df.loc[df["dep_delay"] == maximum["dep_delay"]])
# Tampilkan data penerbangan dengan arr_delay terendah
print(df.loc[df["arr_delay"] == minimum["arr_delay"]])

# LATIHAN-3

# Sort data penerbangan menaik berdasarkan kolom carrier dan terurut menurun berdasarkan kolom flight
df.sort_values(["carrier"], ascending=[1])
df.sort_values(["flight"], ascending=[0])
# Ambil 100 data teratas dari data penerbangan yang terurut menaik berdasarkan kolom distance, untuk data pada month = 5
df_month5 = df.loc[df["month"] == 5] # DataFrame dengan month = 5
df_month5_sort = df_month5.sort_values(["distance"], ascending=[1]) # DataFrame dengan month = 5 yang terurut menaik
df_month5_sort[0:100] # mengambil 100 data teratas

# LATIHAN-4

# Buatlah distribusi frekuensi untuk kolom: month dan distance
df["month"].value_counts()
df["distance"].value_counts()

# LATIHAN-5

# Hitunglah dan amati nilai rata-rata dan deviasi standar pada kolom dep_delay dan arr_delay.
df["dep_delay"].mean() # 9.46377305609211
df["dep_delay"].std() # 36.54510931299814
df["arr_delay"].mean() # 2.0945373495349116
df["arr_delay"].std() # 41.47934870103866
# Tampilkan dan berikan komentar terhadap statistik pada data penerbangan dengan perintah .describe
print(df.describe())
# berdasarkan hasil analisis terhadap statistik pada data penerbangan dengan perintah .describe,
# terlihat bahwa penerbangan rata-rata berdurasi sekitar 12 sampai 13 jam.
# Dengan standar deviasi sebesar 4.725552 jam, menandakan bahwa rentang perbedaan durasi dalam jam tidak begitu besar.

# LATIHAN-6

# Korelasi antara perolehan dep_delay dengan arr_delay. Jelaskan maknanya:
print(df["dep_delay"].corr(df["arr_delay"]))
# Nilai yang mengindikasikan hubungan antara dep_delay dan arr_delay,
# dinyatakan dalam skala -1 sampai 1, dengan -1 berkorelasi sempurna secara terbalik
# dan 1 berkorelasi sempurna secara lurus.
# Nilai dari korelasi di atas adalah 0.890870087347427, sehingga dep_delay dengan arr_delay
# berkorelasi dengan baik secara lurus.
