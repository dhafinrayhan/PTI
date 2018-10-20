# NIM/Nama  : 16518332/Dhafin Rayhan Ahmad
# Tanggal   : 8 September 2018
# Deskripsi : Mencari pemenang dari 3 tim dengan menghitung skor dan membandingkan peraihan medali

# Catatan
# Pada script ini, aturan no. 5 diabaikan karena jika skor, emas, dan perak sama,
# maka otomatis perunggu juga sama.
# Sehingga pembanding jumlah perunggu sudah tersirat pada keumuman algoritma.

# KAMUS
# (berdasarkan instruksi dosen)
# gt: integer, perolehan emas Jawa Tengah
# st: integer, perolehan perak Jawa Tengah
# bt: integer, perolehan perunggu Jawa Tengah
# gb: integer, perolehan emas Jawa Barat
# sb: integer, perolehan perak Jawa Barat
# bb: integer, perolehan perunggu Jawa Barat
# gj: integer, perolehan emas DKI Jakarta
# sj: integer, perolehan perak DKI Jakarta
# bj: integer, perolehan perunggu DKI Jakarta
# tt: integer, skor Jawa Tengah
# tb: integer, skor Jawa Barat
# tj: integer, skor DKI Jakarta
# xt: string, teks "Jawa Tengah."
# xb: string, teks "Jawa Barat."
# xj: string, teks "DKI Jakarta."
# w: string, xt/xb/xj akan dimasukkan nilainya pada variabel ini

# Meminta input medali
gt = int(input("Masukkan perolehan emas Jawa Tengah: "))
st = int(input("Masukkan perolehan perak Jawa Tengah: "))
bt = int(input("Masukkan perolehan perunggu Jawa Tengah: "))
gb = int(input("Masukkan perolehan emas Jawa Barat: "))
sb = int(input("Masukkan perolehan perak Jawa Barat: "))
bb = int(input("Masukkan perolehan perunggu Jawa Barat: "))
gj = int(input("Masukkan perolehan emas DKI Jakarta: "))
sj = int(input("Masukkan perolehan perak DKI Jakarta: "))
bj = int(input("Masukkan perolehan perunggu DKI Jakarta: "))

# Menghitung skor
tt = 3*gt + 2*st + 1*bt
tb = 3*gb + 2*sb + 1*bb
tj = 3*gj + 2*sj + 1*bj

# Teks output pemenang
xt = "Jawa Tengah."
xb = "Jawa Barat."
xj = "DKI Jakarta."

# Variabel pemenang
w = ""

# Membandingkan skor
if tt == tb and tb == tj:
    if gt == gb and gb == gj:
        if st == sb:
            # menggunakan asumsi provinsi unggul
            w = xj
        elif sb == sj:
            # menggunakan asumsi provinsi unggul
            w = xt
        elif sj == st:
            # menggunakan asumsi provinsi unggul
            w = xb
        elif st > sb:
            if sj > st:
                w = xj
            else:
                w = xt
        else: # st < sb
            if sj > sb:
                w = xj
            else:
                w = xb
    elif gt == gb:
        if gj > gt:
            w = xj
        else: # gj < gt
            if st > sb:
                w = xt
            else: # st < sb
                w = xb
    elif gb == gj:
        if gt > gb:
            w = xt
        else: # gt < gb
            if sb > sj:
                w = xb
            else: # sb < sj
                w = xj
    elif gj == gt:
        if gb > gj:
            w = xb
        else: # gb < gj
            if sj > st:
                w = xj
            else: # sj < st
                w = xt
    elif gt > gb:
        if gj > gt:
            w = xj
        else:
            w = xt
    else: # gt < gb
        if gj > gb:
            w = xj
        else:
            w = xb
elif tt == tb: # jika Jawa Tengah dan Jawa Barat seri
    # menggunakan asumsi provinsi unggul
    if tj > tt:
        w = xj
    elif gt == gb:
        if st > sb:
            w = xt
        else:
            w = xb
    elif gt > gb:
        w = xt
    else:
        w = xb
elif tb == tj: # jika Jawa Barat dan DKI Jakarta seri
    # menggunakan asumsi provinsi unggul
    if tt > tb:
        w = xt
    elif gb == gj:
        if sb > sj:
            w = xb
        else:
            w = xj
    elif gb > gj:
        w = xb
    else:
        w = xj
elif tj == tt: # jika DKI Jakarta dan Jawa Tengah seri
    # menggunakan asumsi provinsi unggul
    if tb > tj:
        w = xb
    elif gj == gt:
        if sj > st:
            w = xj
        else:
            w = xt
    elif gj > gt:
        w = xj
    else:
        w = xt
elif tt > tb: # jika Jawa Tengah lebih unggul dari Jawa Barat
    if tj > tt: # jika DKI Jakarta lebih unggul dari Jawa Tengah
        w = xj
    else:
        w = xt
else: # jika Jawa Barat lebih unggul dari Jawa Tengah
    if tj > tb: # jika DKI Jakarta lebih unggul dari Jawa Barat
        w = xj
    else:
        w = xb

# Output pemenang
print("Pemenangnya adalah " + w)
