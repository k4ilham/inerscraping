@echo off
echo ==========================================
echo    Web Scraper Runner - Inercorp
echo ==========================================
echo.

echo [1/3] Memeriksa dependensi...
python -m pip install -r requirements.txt

echo.
echo [2/3] Menjalankan Scraper...
python scraper.py

echo.
echo [3/3] Selesai! 
echo Hasil dapat dilihat di folder ini.
echo.
pause
