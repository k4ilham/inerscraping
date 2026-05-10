#!/bin/bash
echo "=========================================="
echo "   Web Scraper Runner - Inercorp"
echo "=========================================="
echo ""

echo "[1/3] Memeriksa dependensi..."
# Menggunakan python3 karena Linux/Mac biasanya memisahkan python2 dan python3
python3 -m pip install -r requirements.txt

echo ""
echo "[2/3] Menjalankan Scraper..."
python3 scraper.py

echo ""
echo "[3/3] Selesai!"
echo "Hasil dapat dilihat di folder ini."
