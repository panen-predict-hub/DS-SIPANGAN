# SIPangan Analytics

**SIPangan Analytics** adalah dashboard interaktif berbasis **Streamlit** yang digunakan untuk menganalisis harga pangan di Provinsi Jawa Timur. Dashboard ini membantu pengguna memahami pola harga pangan berdasarkan **komoditas, wilayah, dan periode waktu** melalui visualisasi yang ringkas, informatif, dan mudah digunakan.

Project ini dikembangkan untuk mendukung proses pemantauan harga pangan serta menjadi dasar awal dalam pengembangan sistem analisis dan prediksi harga pangan pada platform **SIPangan**.

---

## Overview Project

Harga pangan merupakan salah satu aspek penting dalam pemantauan stabilitas ekonomi dan ketahanan pangan daerah. Perubahan harga yang terlalu tinggi atau tidak stabil dapat berdampak pada masyarakat, pelaku usaha, hingga pengambil kebijakan.

Melalui project ini, data harga pangan Jawa Timur dibersihkan, digabungkan, dianalisis, dan divisualisasikan ke dalam dashboard interaktif. Dashboard ini memungkinkan pengguna untuk melihat ringkasan harga, membandingkan antarwilayah, memahami tren historis, serta melihat estimasi sederhana harga bulan berikutnya.

---

## Tujuan Project

Tujuan utama dari project ini adalah:

- Menyiapkan dataset harga pangan Jawa Timur agar siap digunakan untuk analisis.
- Menggabungkan data historis dari Kaggle dengan data tambahan terbaru dari BPS.
- Menganalisis harga pangan berdasarkan komoditas, wilayah, dan periode.
- Menampilkan insight utama melalui visualisasi interaktif.
- Membantu pengguna memantau wilayah dan komoditas yang memiliki harga tinggi atau fluktuasi besar.
- Menyediakan dataset final yang dapat digunakan untuk dashboard dan pengembangan analisis lanjutan.

---

## Dataset

Dataset yang digunakan dalam project ini berasal dari dua sumber utama:

1. **Kaggle - Harga Pertanian Jawa Timur**  
   Dataset historis harga pertanian Jawa Timur.

2. **Data Tambahan BPS**  
   Data tambahan yang digunakan untuk melengkapi periode terbaru agar cakupan data menjadi lebih panjang dan relevan.

Dataset final yang digunakan oleh dashboard berada pada path berikut:

```text
data/data_final.csv
