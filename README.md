<br />
<div align="center">
  <h2 align="center">🌊 Raspi-SERIBU</h2>
  <p align="center">
    <em><strong>S</strong>tream <strong>E</strong>cosystem <strong>R</strong>eal-time <strong>I</strong>ntegrated <strong>B</strong>aseline <strong>U</strong>tility</em><br>
    <strong>Otomatisasi deteksi dan pelaporan sampah di sungai menggunakan Raspberry Pi.</strong>
  </p>
</div>


---

## 🔍 Overview

**Raspi-SERIBU** adalah sistem otomatis berbasis Raspberry Pi yang dirancang untuk mendeteksi dan melaporkan keberadaan sampah di sungai secara berkala. Dengan memanfaatkan kamera dan algoritma sederhana, alat ini menangkap gambar kondisi sungai dan mengirimkannya ke server untuk diproses lebih lanjut.

> Solusi ini ditujukan untuk mendukung monitoring lingkungan secara real-time, terutama di wilayah aliran sungai (DAS) yang rawan pencemaran.

---

## ⚙️ Fitur Utama

- 📸 Pengambilan gambar otomatis dengan interval tertentu  
- 🌐 Pengiriman gambar dan data lingkungan ke server  
- 📡 Dukungan integrasi dengan sistem pelaporan atau dashboard monitoring  
- 🔁 Dapat berjalan terus-menerus tanpa interaksi manual  
- 💡 Konsumsi daya rendah, cocok untuk sistem IoT

---

## 🚀 Instalasi

Ikuti langkah-langkah berikut untuk menginstal proyek secara lokal:

### 1. Clone repositori

```bash
git clone https://github.com/Dhaboav/raspi-seribu.git
cd raspi-seribu
```

### 2. Instal dependensi Python
 ```bash 
 pip install -r requirements.txt
 ```

 ### 3. Konfigurasi environment
 ```bash 
 copy .env.example .env
 ```

---

## 💻 Penggunaan

Untuk menjalankan sistem secara terus-menerus:

```bash
python main.py
```
## 🏆 Tentang Proyek

SERIBU dikembangkan sebagai solusi monitoring lingkungan berbasis teknologi IoT.
Proyek ini bertujuan membantu pengawasan dan pelaporan sampah di sungai secara efisien dan real-time, dengan biaya rendah dan mudah diimplementasikan.

> Proyek ini dibuat dalam rangka mendukung inisiatif digitalisasi lingkungan, serta sebagai bagian dari kontribusi dalam ajang Gemastik dan pengabdian masyarakat berbasis teknologi.
