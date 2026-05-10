# Inercorp News Scraper

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Skrip otomatisasi web scraping untuk mengumpulkan berita dari berbagai sumber Indonesia (Multi-Source) secara lengkap dan terstruktur.

## ✨ Fitur Utama
- **Multi-Source**: Mengambil berita dari RSS Feed (Kompas, Antara, Liputan6, Tempo, dll) dan Detik Search.
- **Full Content**: Mengekstrak isi berita lengkap (bukan ringkasan) menggunakan library `newspaper3k`.
- **Smart Deduplication**: Menghindari berita ganda berdasarkan judul dan URL.
- **Progressive CLI**: Dilengkapi dengan Progress Bar (`tqdm`) untuk memantau proses secara real-time.
- **Configurable**: Rentang tahun (2020-2026), kata kunci, dan sumber berita dapat diatur dengan mudah.

## 🚀 Cara Penggunaan Cepat
1. Masukkan kata kunci di `keyword.txt`.
2. Klik dua kali file `run.bat`.
3. Hasil akhir tersedia di `dataset.csv`.

## 📂 Struktur Proyek
- `scraper.py`: Mesin utama scraping.
- `config.py`: Pengaturan sistem dan sumber berita.
- `manualbook.md`: Panduan lengkap dengan instruksi gambar.
- `keyword.txt`: Daftar target pencarian.

## 📖 Panduan Lengkap
Untuk instruksi lebih detail beserta gambar petunjuk, silakan baca:
👉 **[Manual Book (manualbook.md)](manualbook.md)**

---
*Developed for Inercorp - 2026*
