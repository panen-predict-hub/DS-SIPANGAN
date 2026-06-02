# SIPangan Analytics

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-green)

**SIPangan Analytics** adalah dashboard interaktif berbasis **Streamlit** untuk menganalisis harga pangan di Provinsi Jawa Timur. Dashboard ini menampilkan ringkasan harga pangan, perbandingan antarwilayah, tren historis, estimasi sederhana harga bulan berikutnya, serta data hasil filter yang dapat diunduh.

Project ini dibuat untuk menyiapkan dan menganalisis data harga pangan Jawa Timur agar lebih mudah dipahami melalui dashboard interaktif. Dengan adanya dashboard ini, data harga pangan tidak hanya ditampilkan dalam bentuk tabel, tetapi juga divisualisasikan agar pola harga berdasarkan komoditas, wilayah, dan periode dapat dibaca dengan lebih jelas.

---

## Daftar Isi

- [Tujuan Project](#tujuan-project)
- [Sumber Data](#sumber-data)
- [Dataset Final](#dataset-final)
- [Struktur Folder](#struktur-folder)
- [Susunan File Project](#susunan-file-project)
- [Keterangan File](#keterangan-file)
- [Environment](#environment)
- [Cara Menjalankan Dashboard](#cara-menjalankan-dashboard)
- [Fitur Dashboard](#fitur-dashboard)
- [Ringkasan Proses Analisis](#ringkasan-proses-analisis)
- [Catatan Penting](#catatan-penting)
- [Deployment](#deployment)
- [Status Project](#status-project)
- [Author](#author)

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

Data yang digunakan berasal dari dua sumber utama.

### 1. Kaggle - Harga Pertanian Jawa Timur

Dataset utama berasal dari Kaggle:

```text
Harga Pertanian Jawa Timur
```

Link dataset:

```text
https://www.kaggle.com/datasets/rakafal/harga-pertanian-jawa-timur
```

Dataset ini digunakan sebagai data historis awal untuk menganalisis harga pangan di Provinsi Jawa Timur.

### 2. Data Tambahan BPS

Data tambahan BPS digunakan untuk melengkapi periode data terbaru. Data tambahan ini sudah disimpan di dalam folder `data`, sehingga project dapat dijalankan tanpa perlu mengakses Google Drive pribadi.

---

## Dataset Final

Dataset final yang digunakan oleh dashboard berada di:

```text
data/data_final.csv
```

Dataset final ini merupakan hasil dari proses penggabungan, cleaning, penyesuaian format, dan persiapan data untuk kebutuhan dashboard.

Dataset akhir digunakan sebagai sumber utama pada aplikasi Streamlit.

---

## Struktur Folder

Struktur folder project:

```text
SIPangan/
├── main.py
├── requirements.txt
├── README.md
├── SIPangan.ipynb
└── data/
    ├── data_bps.csv
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

## Susunan File Project

Berikut susunan file utama dalam project **SIPangan Analytics**:

```text
SIPangan/
│
├── main.py
│   └── File utama untuk menjalankan dashboard Streamlit.
│
├── requirements.txt
│   └── Berisi daftar library yang dibutuhkan untuk menjalankan dashboard.
│
├── README.md
│   └── Dokumentasi project.
│
├── SIPangan.ipynb
│   └── Notebook yang berisi proses analisis data dari awal sampai akhir.
│
└── data/
    │
    ├── data_bps.csv
    │   └── Data mentah tambahan dari BPS.
    │
    ├── data_gabungan.csv
    │   └── Data hasil gabungan dari Kaggle dan data tambahan BPS.
    │
    ├── data_clean.csv
    │   └── Data yang sudah melalui proses cleaning.
    │
    ├── data_final.csv
    │   └── Dataset final yang digunakan oleh dashboard.
    │
    └── data_dictionary.csv
        └── Penjelasan kolom pada dataset final.
```

---

## Keterangan File

| File | Keterangan |
|---|---|
| `main.py` | File utama untuk menjalankan dashboard Streamlit. |
| `requirements.txt` | Daftar library yang dibutuhkan untuk menjalankan dashboard. |
| `README.md` | Dokumentasi project. |
| `SIPangan.ipynb` | Notebook yang berisi proses analisis data dari awal sampai akhir. |
| `data/data_bps.csv` | Data mentah tambahan dari BPS. |
| `data/data_gabungan.csv` | Data hasil gabungan dari Kaggle dan BPS. |
| `data/data_clean.csv` | Data yang sudah melalui proses cleaning. |
| `data/data_final.csv` | Dataset final yang digunakan oleh dashboard. |
| `data/data_dictionary.csv` | Penjelasan kolom pada dataset final. |

---

## Environment

Dashboard ini membutuhkan Python dan beberapa library berikut:

```text
streamlit
pandas
numpy
plotly
```

Semua library tersebut sudah ditulis di dalam file:

```text
requirements.txt
```

Fungsi utama library:

| Library | Fungsi |
|---|---|
| `streamlit` | Membuat dashboard interaktif berbasis web. |
| `pandas` | Membaca, mengolah, membersihkan, dan menganalisis data. |
| `numpy` | Mendukung proses komputasi numerik. |
| `plotly` | Membuat visualisasi interaktif pada dashboard. |

---

## Cara Menjalankan Dashboard

### 1. Clone atau Download Repository

Clone repository:

```bash
git clone <link-repository>
```

Masuk ke folder project:

```bash
cd SIPangan
```

Jika folder `SIPangan` berada di dalam folder repository lain, masuk ke folder sesuai lokasinya.

Contoh:

```bash
cd nama-repo/SIPangan
```

---

### 2. Install Library

Jalankan perintah berikut di terminal atau CMD:

```bash
pip install -r requirements.txt
```

Jika `pip` tidak terbaca, gunakan:

```bash
python -m pip install -r requirements.txt
```

---

### 3. Jalankan Dashboard

Jalankan dashboard:

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

Dashboard **SIPangan Analytics** terdiri dari beberapa fitur utama.

---

### 1. Overview

Menu **Overview** menampilkan ringkasan umum harga pangan.

Informasi yang ditampilkan pada bagian ini meliputi:

- jumlah data,
- jumlah wilayah,
- jumlah komoditas,
- rata-rata harga,
- periode data,
- prioritas pemantauan komoditas,
- dan tren harga semua komoditas.

Bagian ini membantu pengguna memahami kondisi umum dataset dan melihat komoditas mana yang memiliki harga tinggi atau fluktuasi besar.

---

### 2. Perbandingan Wilayah

Menu **Perbandingan Wilayah** menampilkan perbandingan seluruh wilayah berdasarkan komoditas yang dipilih.

Bagian ini menunjukkan:

- wilayah dengan rata-rata harga tertinggi,
- wilayah dengan fluktuasi harga tertinggi,
- serta ringkasan otomatis berdasarkan hasil perbandingan.

Fitur ini berguna untuk melihat wilayah mana yang perlu mendapatkan perhatian lebih dalam pemantauan harga pangan.

---

### 3. Tren & Estimasi

Menu **Tren & Estimasi** menampilkan tren harga berdasarkan komoditas dan wilayah tertentu.

Pada bagian ini, pengguna dapat memilih:

- komoditas,
- wilayah,
- dan rentang tahun.

Estimasi sederhana harga bulan berikutnya dihitung menggunakan rata-rata tiga bulan terakhir. Estimasi ini masih bersifat sederhana dan belum menggantikan model forecasting, tetapi dapat digunakan sebagai gambaran awal arah harga.

---

### 4. Data

Menu **Data** menampilkan data hasil filter berdasarkan:

- komoditas,
- wilayah,
- dan rentang tahun.

Data hasil filter juga dapat diunduh dalam format CSV, sehingga pengguna dapat menggunakan kembali data tersebut untuk kebutuhan analisis lanjutan.

---

## Ringkasan Proses Analisis

Proses analisis dilakukan dalam notebook:

```text
SIPangan.ipynb
```

Tahapan analisis yang dilakukan:

---

### 1. Business Understanding

Menentukan tujuan project dan kebutuhan analisis.

Pada tahap ini, fokus utama project adalah memahami kebutuhan pemantauan harga pangan berdasarkan:

- komoditas,
- wilayah,
- dan periode.

---

### 2. Data Gathering

Mengambil data dari Kaggle dan data tambahan BPS.

Data Kaggle digunakan sebagai data historis utama, sedangkan data tambahan BPS digunakan untuk melengkapi periode terbaru.

---

### 3. Assessing Data

Mengecek kondisi awal dataset sebelum dilakukan cleaning.

Pengecekan dilakukan terhadap:

- struktur data,
- jumlah baris dan kolom,
- periode data,
- kategori komoditas,
- wilayah,
- missing value,
- nilai nol,
- dan duplikasi.

Tahap ini bertujuan untuk mengetahui masalah yang ada pada dataset sebelum data diproses lebih lanjut.

---

### 4. Cleaning Data

Merapikan data agar lebih konsisten dan siap dianalisis.

Proses cleaning dilakukan dengan menyesuaikan format data, merapikan nama kategori, memastikan data tersusun berdasarkan wilayah dan periode, serta menyiapkan dataset agar dapat digunakan pada dashboard.

---

### 5. Feature Engineering

Menambahkan fitur pendukung seperti:

- `tahun`,
- `bulan`,
- `tahun_bulan`,
- dan `series_id`.

Fitur tambahan ini digunakan untuk membantu proses filter, visualisasi, dan analisis time series.

---

### 6. Data Dictionary

Membuat penjelasan kolom dataset final.

Data dictionary dibuat agar pengguna dapat memahami arti setiap kolom yang terdapat pada dataset final.

---

### 7. EDA dan Visualisasi

Menganalisis pola harga berdasarkan:

- waktu,
- komoditas,
- dan wilayah.

Visualisasi dibuat untuk membantu membaca pola harga, melihat perbandingan antarwilayah, serta memahami perubahan harga dari waktu ke waktu.

---

### 8. Conclusion

Merangkum hasil utama dari analisis.

Kesimpulan dibuat berdasarkan hasil cleaning, EDA, dan visualisasi yang telah dilakukan.

---

### 9. Dashboard Preparation

Menyiapkan file dashboard, requirements, dan dataset final.

Tahap ini memastikan bahwa file yang diperlukan untuk menjalankan dashboard sudah tersedia dan tersusun dengan benar.

---

### 10. A/B Testing Dashboard

Membandingkan dashboard versi awal dan versi final berdasarkan kriteria penilaian.

Tahap ini dilakukan untuk melihat apakah dashboard final lebih baik dari sisi tampilan, struktur informasi, kemudahan penggunaan, dan penyampaian insight.

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

Untuk deployment yang lebih aman, path dataset dapat dibuat menggunakan lokasi file `main.py`:

```python
import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "data", "data_final.csv")

data = pd.read_csv(DATA_PATH)
```

Data BPS sudah disimpan di folder `data`, sehingga pengguna lain tidak perlu mengakses Google Drive pribadi.

---

## Deployment

Dashboard dapat dijalankan secara lokal atau dideploy menggunakan **Streamlit Community Cloud**.

Jika struktur repository seperti ini:

```text
repo/
└── SIPangan/
    ├── main.py
    ├── requirements.txt
    └── data/
        └── data_final.csv
```

Maka main file path pada Streamlit Cloud adalah:

```text
SIPangan/main.py
```

Jika `main.py` berada langsung di root repository:

```text
repo/
├── main.py
├── requirements.txt
└── data/
    └── data_final.csv
```

Maka main file path pada Streamlit Cloud adalah:

```text
main.py
```

---

## Status Project

Status pengerjaan project:

| Tahapan | Status |
|---|---|
| Data Gathering | Selesai |
| Assessing Data | Selesai |
| Cleaning Data | Selesai |
| Feature Engineering | Selesai |
| Data Dictionary | Selesai |
| EDA dan Visualisasi | Selesai |
| Conclusion | Selesai |
| Dashboard Preparation | Selesai |
| A/B Testing Dashboard | Selesai |
| Deployment Streamlit | Siap / Dalam proses |

---

## Author

Project ini dikembangkan sebagai bagian dari analisis data harga pangan Jawa Timur.

**SIPangan Analytics**  
Dashboard Analisis Harga Pangan Jawa Timur
