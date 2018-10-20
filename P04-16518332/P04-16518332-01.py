# NIM/Nama	: Dhafin Rayhan Ahmad
# Tanggal	: Deskripsi
# Deskripsi	: Analisis data transaksi suatu toko menggunakan module 'pandas'

# Import module yang diperlukan, yaitu 'pandas' dengan alias 'pd'
import pandas as pd

# Baca file "data.csv"
df = pd.read_csv("data.csv")

# 1. Banyaknya data
print(len(df))
# 10000

# 2. Transaksi yang dilakukan oleh Tuan Yon
print(df.loc[df["nama"] == "Tuan Yon"])
#           nama tipe_barang  bulan  tahun  qty  profit
# 4390  Tuan Yon  elektronik      4   2017    7  199999

# 3. Banyaknya transaksi dengan profit di atas 150.000
print(len(df.loc[df["profit"] > 150000]))
# 2656

# 4. Banyaknya transaksi di bulan Oktober 2014 dengan quantitiy kurang dari 10
print(len(df.loc[(df["bulan"] == 10) & (df["tahun"] == 2014) & (df["qty"] < 10)])) # Oktober = 10
# 45

# 5. Banyaknya transaksi makanan dengan profit minimum
df_makanan = df.loc[df["tipe_barang"] == "makanan"] # DataFrame yang hanya memuat data dengan tipe_barang = 'makanan'
i_profit_min_makanan = df_makanan["profit"].idxmin() # index dari data dengan profit minimum dari DF di atas
profit_min_makanan = df_makanan.loc[i_profit_min_makanan, "profit"] # nilai dari profit minimal
print(len(df_makanan.loc[df["profit"] == profit_min_makanan]))
# 1

# 6. Data 10 transaksi alat makan dengan profit terbesar di tahun 2017
df_alatmakan_2017 = df.loc[(df["tipe_barang"] == "alat makan") & (df["tahun"] == 2017)] # DataFrame yang hanya memuat data dengan tipe_barang = 'alat makan' dan tahun = 2017
df_alatmakan_2017_sortdc = df_alatmakan_2017.sort_values(["profit"], ascending=[0]) # mengurutkan DF di atas berdasarkan profit secara descending
print(df_alatmakan_2017_sortdc[0:10]) # mencetak 10 data pertama dalam df_alatmakan_2017_sortdc
#                             nama tipe_barang  bulan  tahun  qty  profit
# 1433      Elfa Norisda Aulianisa  alat makan     12   2017   20  197810
# 6122       Rian Jamaludin Pogram  alat makan      4   2017   20  196871
# 8393       Destria Nur Imaniarti  alat makan      8   2017   20  196614
# 2557               Raihan Faisya  alat makan      7   2017   20  196324
# 1926  Muhammad Fikry Nashiruddin  alat makan      6   2017   20  193587
# 7602            Okaswara Perkasa  alat makan      1   2017   20  192937
# 4016           Hary Yady Pratama  alat makan     11   2017   19  188155
# 9100             Nadiya Azkanisa  alat makan      2   2017   19  187000
# 6021            Amelinda A A V K  alat makan      1   2017   19  186531
# 3413        Muhammad Arif Furqon  alat makan     10   2017   19  183769

# 7. Tabel frekuensi masing-masing tahun
print(df["tahun"].value_counts())
# 2010    1300
# 2015    1290
# 2012    1281
# 2013    1250
# 2017    1238
# 2014    1226
# 2016    1213
# 2011    1202
# Name: tahun, dtype: int64

# 8. Rata-rata profit di bulan Desember 2016
df_Des2016 = df.loc[(df["bulan"] == 12) & (df["tahun"] == 2016)] # DataFrame yang hanya memuat data dengan bulan = 12 dan tahun = 2016
print(df_Des2016["profit"].mean())
# 106113.73809523809

# 9. Standar deviasi dari profit transaksi pakaian
df_pakaian = df.loc[df["tipe_barang"] == "pakaian"] # DataFrame yang hanya memuat data dengan tipe_barang = 'pakaian'
print(df_pakaian["profit"].std())
# 55454.802489044356

# 10. Rata-rata dari profit transaksi pakaian sebelum tahun 2016
df_pakaian_b2016 = df.loc[(df["tipe_barang"] == "pakaian") & (df["tahun"] < 2016)] # DataFrame yang hanya memuat data dengan tipe_barang = 'pakaian' dan tahun < 2016
print(df_pakaian_b2016["profit"].mean())
# 105296.03875134554

# 11. Koefisien korelasi dari quantity dengan profit
print(df["qty"].corr(df["profit"]))
# 0.9983687460949128
