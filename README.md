# SiPangan Analytics

SiPangan Analytics adalah dashboard interaktif berbasis Streamlit untuk menganalisis harga pangan di Provinsi Jawa Timur.

Dashboard ini menampilkan ringkasan harga pangan, perbandingan antarwilayah, tren historis, estimasi sederhana harga bulan berikutnya, serta data hasil filter yang dapat diunduh.

## Tujuan Project

Project ini dibuat untuk:

- Menyiapkan data harga pangan Jawa Timur agar siap dianalisis.
- Menggabungkan data dari Kaggle dan data tambahan BPS.
- Menganalisis harga pangan berdasarkan komoditas, wilayah, dan periode.
- Menampilkan insight utama melalui dashboard interaktif.
- Menyediakan dataset final untuk dashboard dan analisis lanjutan.

## Sumber Data

Data yang digunakan berasal dari:

1. Kaggle - Harga Pertanian Jawa Timur  
   https://www.kaggle.com/datasets/rakafal/harga-pertanian-jawa-timur

2. Data tambahan BPS  
   Data ini digunakan untuk melengkapi periode data terbaru.

Dataset final yang digunakan dashboard berada di:

```text
data/data_final.csv
```

Data BPS juga sudah disimpan di folder `data`, sehingga project dapat dijalankan tanpa perlu mengakses Google Drive pribadi.

## Struktur Folder

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

File minimal agar dashboard dapat berjalan:

```text
main.py
requirements.txt
data/data_final.csv
```

## Keterangan File

- `main.py`: file utama dashboard Streamlit.
- `requirements.txt`: daftar library untuk menjalankan dashboard.
- `SiPangan.ipynb`: notebook proses analisis data.
- `data/data_final.csv`: dataset final yang digunakan dashboard.
- `data/data_dictionary.csv`: penjelasan kolom dataset final.
- `data/data_clean.csv`: data hasil cleaning.
- `data/data_gabungan.csv`: data gabungan dari Kaggle dan BPS.
- `data/data_raw_bps.csv`: data mentah tambahan dari BPS.

## Environment

Dashboard membutuhkan library berikut:

```text
streamlit
pandas
numpy
plotly
```

Semua library sudah tersedia di file `requirements.txt`.

## Cara Menjalankan Dashboard

Clone atau download repository, lalu masuk ke folder project:

```bash
cd SiPangan
```

Install library:

```bash
pip install -r requirements.txt
```

Jika `pip` tidak terbaca, gunakan:

```bash
python -m pip install -r requirements.txt
```

Jalankan dashboard:

```bash
streamlit run main.py
```

Jika `streamlit` tidak terbaca, gunakan:

```bash
python -m streamlit run main.py
```

Dashboard akan terbuka di browser melalui:

```text
http://localhost:8501
```

## Fitur Dashboard

### Overview

Menampilkan ringkasan umum harga pangan, jumlah data, jumlah wilayah, jumlah komoditas, rata-rata harga, periode data, prioritas pemantauan komoditas, dan tren harga semua komoditas.

### Perbandingan Wilayah

Menampilkan perbandingan seluruh wilayah berdasarkan komoditas yang dipilih, termasuk wilayah dengan rata-rata harga tertinggi dan fluktuasi harga tertinggi.

### Tren & Estimasi

Menampilkan tren harga berdasarkan komoditas dan wilayah tertentu. Estimasi sederhana harga bulan berikutnya dihitung menggunakan rata-rata tiga bulan terakhir.

### Data

Menampilkan data hasil filter berdasarkan komoditas, wilayah, dan rentang tahun. Data hasil filter dapat diunduh dalam format CSV.

## Ringkasan Proses Analisis

Proses analisis dilakukan dalam notebook `SiPangan.ipynb`.

Tahapan utama:

1. Business Understanding
2. Data Gathering
3. Assessing Data
4. Cleaning Data
5. Feature Engineering
6. Data Dictionary
7. EDA dan Visualisasi
8. Conclusion
9. Dashboard Preparation
10. A/B Testing Dashboard

## Catatan Penting

Agar dashboard tidak error:

- Pastikan `data_final.csv` berada di folder `data`.
- Jangan menghapus `requirements.txt`.
- Jangan memindahkan file CSV keluar dari folder `data`.
- Jangan mengubah nama `data_final.csv` tanpa menyesuaikan path di `main.py`.

Di dalam `main.py`, dataset dibaca dari:

```python
pd.read_csv("data/data_final.csv")
```

## Author

Project ini dikembangkan sebagai bagian dari analisis data harga pangan Jawa Timur.
