# SiPangan Analytics
SiPangan Analytics adalah dashboard interaktif berbasis Streamlit untuk menganalisis harga pangan di Provinsi Jawa Timur. Dashboard ini menampilkan ringkasan harga pangan, perbandingan antarwilayah, tren historis, estimasi sederhana harga bulan berikutnya, serta data hasil filter yang dapat diunduh.
---

## Tujuan Project
Project ini dibuat untuk menyiapkan dan menganalisis data harga pangan Jawa Timur agar lebih mudah dipahami melalui dashboard interaktif.
Tujuan utama project ini adalah:
- Menyiapkan data harga pangan Jawa Timur agar siap dianalisis.
- Menggabungkan data dari Kaggle dan data tambahan BPS.
- Menganalisis harga pangan berdasarkan komoditas, wilayah, dan periode.
- Menampilkan insight utama melalui visualisasi dan dashboard interaktif.
- Menyediakan dataset final yang dapat digunakan untuk dashboard dan analisis lanjutan.

---

## Sumber Data
Data yang digunakan berasal dari dua sumber utama:
1. Kaggle - Harga Pertanian Jawa Timur
   https://www.kaggle.com/datasets/rakafal/harga-pertanian-jawa-timur
2. Data tambahan BPS
   Data tambahan ini digunakan untuk melengkapi periode data terbaru.
Dataset final yang digunakan oleh dashboard berada di:
```text
data/data_final.csv
```
Data BPS juga sudah disimpan di folder `data`, sehingga project dapat dijalankan tanpa perlu mengakses Google Drive pribadi.
---

## Struktur Folder
Struktur folder project:
```text
SiPangan/
├── main.py
├── requirements.txt
├── README.md
├── SiPangan.ipynb
└── data/
    ├── data_raw_bps.csv
    ├── data_gabungan.csv
    ├── data_clean.csv
    ├── data_final.csv
    └── data_dictionary.csv
```
File minimal yang wajib ada agar dashboard dapat berjalan:
```text
main.py
requirements.txt
data/data_final.csv
```

---
## Keterangan File
`main.py`
File utama untuk menjalankan dashboard Streamlit.
`requirements.txt`
Daftar library yang dibutuhkan untuk menjalankan dashboard.
`SiPangan.ipynb`
Notebook yang berisi proses analisis data dari awal sampai akhir.
`data/data_final.csv`
Dataset final yang digunakan oleh dashboard.
`data/data_dictionary.csv`
Penjelasan kolom pada dataset final.
`data/data_clean.csv`
Data yang sudah melalui proses cleaning.
`data/data_gabungan.csv`
Data gabungan dari Kaggle dan BPS.
`data/data_raw_bps.csv`
Data mentah tambahan dari BPS.
---

## Environment
Dashboard ini membutuhkan Python dan beberapa library berikut:
```text
streamlit
pandas
numpy
plotly
```
Semua library tersebut sudah ditulis di dalam file `requirements.txt`.
---

## Cara Menjalankan Dashboard
### 1. Clone atau download repository
Clone repository:
```bash
git clone <link-repository>
```
Masuk ke folder project:
```bash
cd SiPangan
```
Jika folder `SiPangan` berada di dalam folder repository lain, masuk ke folder sesuai lokasinya.
Contoh:
```bash
cd nama-repo/SiPangan
```

---
### 2. Install library
Jalankan perintah berikut di terminal atau CMD:
```bash
pip install -r requirements.txt
```
Jika `pip` tidak terbaca, gunakan:
```bash
python -m pip install -r requirements.txt
```

---
### 3. Jalankan dashboard
Jalankan:
```bash
streamlit run main.py
```
Jika `streamlit` tidak terbaca, gunakan:
```bash
python -m streamlit run main.py
```
Setelah berhasil, dashboard akan terbuka di browser melalui alamat:
```text
http://localhost:8501
```

---
## Fitur Dashboard
### Overview
Menampilkan ringkasan umum harga pangan, jumlah data, jumlah wilayah, jumlah komoditas, rata-rata harga, periode data, prioritas pemantauan komoditas, dan tren harga semua komoditas.

### Perbandingan Wilayah
Menampilkan perbandingan seluruh wilayah berdasarkan komoditas yang dipilih. Bagian ini menunjukkan wilayah dengan rata-rata harga tertinggi dan wilayah dengan fluktuasi harga tertinggi.

### Tren & Estimasi
Menampilkan tren harga berdasarkan komoditas dan wilayah tertentu. Estimasi sederhana harga bulan berikutnya dihitung menggunakan rata-rata tiga bulan terakhir.

### Data
Menampilkan data hasil filter berdasarkan komoditas, wilayah, dan rentang tahun. Data hasil filter juga dapat diunduh dalam format CSV.
---

## Ringkasan Proses Analisis
Proses analisis dilakukan dalam notebook `SiPangan.ipynb`.
Tahapan analisis yang dilakukan:

1. Business Understanding
   Menentukan tujuan project dan kebutuhan analisis.
2. Data Gathering
   Mengambil data dari Kaggle dan data tambahan BPS.
3. Assessing Data
   Mengecek struktur data, periode, kategori, wilayah, missing value, nilai nol, dan duplikasi.
4. Cleaning Data
   Merapikan data agar lebih konsisten dan siap dianalisis.
5. Feature Engineering
   Menambahkan fitur pendukung seperti `tahun`, `bulan`, `tahun_bulan`, dan `series_id`.
6. Data Dictionary
   Membuat penjelasan kolom dataset final.
7. EDA dan Visualisasi
   Menganalisis pola harga berdasarkan waktu, komoditas, dan wilayah.
8. Conclusion
   Merangkum hasil utama dari analisis.
9. Dashboard Preparation
   Menyiapkan file dashboard, requirements, dan dataset final.
10. A/B Testing Dashboard
   Membandingkan dashboard versi awal dan versi final berdasarkan kriteria penilaian.
---

## Catatan Penting
Agar dashboard tidak error, pastikan:
- File `data_final.csv` berada di folder `data`.
- File `requirements.txt` tidak dihapus.
- File CSV tidak dipindahkan keluar dari folder `data`.
- Nama file `data_final.csv` tidak diubah tanpa menyesuaikan path di `main.py`.

Di dalam `main.py`, dataset dibaca dari:
```python
pd.read_csv("data/data_final.csv")
```
Data raw BPS sudah disimpan di folder `data`, sehingga pengguna lain tidak perlu mengakses Google Drive pribadi.
---

## Author

Project ini dikembangkan sebagai bagian dari analisis data harga pangan Jawa Timur.
