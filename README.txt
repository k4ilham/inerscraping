===========================================================
     MULTI-SOURCE NEWS SCRAPER - INERCORP
===========================================================

Skrip ini digunakan untuk mengambil berita lengkap dari berbagai sumber
berita Indonesia (Multi-Source) berdasarkan kata kunci tertentu.

--- STRUKTUR FILE ---

1. scraper.py     : Skrip utama untuk menjalankan proses scraping.
2. config.py      : File pengaturan (Tahun, RSS Feeds, Jumlah Halaman).
3. keyword.txt    : Daftar kata kunci pencarian (Satu per baris).
4. requirements.txt: Daftar library Python yang dibutuhkan.
5. run.bat        : Shortcut untuk menjalankan program di Windows.
6. dataset.csv    : Database utama hasil scraping (Otomatis dibuat/diperbarui).
7. README.txt     : Panduan penggunaan ini.

--- CARA PENGGUNAAN ---

1. Masukkan kata kunci yang ingin dicari ke dalam file 'keyword.txt'.
2. (Opsional) Sesuaikan rentang tahun atau sumber di 'config.py'.
3. Jalankan file 'run.bat' dengan cara klik dua kali.
4. Tunggu hingga Progress Bar di terminal mencapai 100%.

--- FITUR UNGGULAN ---

- Multi-Source: Mengambil dari Detik, Kompas, Antara, Liputan6, dan lainnya.
- Anti-Duplikat: Berita dengan judul yang sama akan otomatis dilewati.
- Full Content: Mengambil teks berita secara lengkap (bukan hanya ringkasan).
- CLI Progress: Menampilkan progress bar dan status loading secara real-time.
- Dataset Sync: Hasil akan otomatis digabung ke dalam file 'dataset.csv'.

--- PERSYARATAN ---

- Python 3.x
- Koneksi Internet

===========================================================
