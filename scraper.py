import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os
from datetime import datetime
from newspaper import Article
import feedparser
import time
from tqdm import tqdm
import config

def get_full_content(url):
    """Mengambil konten berita lengkap menggunakan newspaper3k."""
    try:
        article = Article(url, language='id')
        article.download()
        article.parse()
        return article.text
    except:
        return ""

def scrape_rss(keywords, seen_titles, seen_urls):
    """Mengambil berita dari RSS Feed dan memfilter berdasarkan kata kunci."""
    results = []
    print(f"\n[1/2] Memeriksa RSS Feeds...")
    
    for feed_url in tqdm(config.RSS_FEEDS, desc="Checking Sources"):
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                url = entry.link
                title = entry.title
                
                # Cek duplikat awal
                if url in seen_urls or title.lower() in seen_titles:
                    continue
                
                # Filter kata kunci
                if any(kw.lower() in title.lower() for kw in keywords):
                    content = get_full_content(url)
                    if content:
                        results.append({
                            'judul': title,
                            'tanggal': entry.published if 'published' in entry else datetime.now().strftime("%d %B %Y"),
                            'isi': content,
                            'sumber': feed.feed.title if 'title' in feed.feed else "RSS",
                            'url': url
                        })
                        seen_urls.add(url)
                        seen_titles.add(title.lower())
        except:
            continue
    return results

def scrape_detik_search(keyword, seen_titles, seen_urls):
    """Pencarian spesifik Detik dengan filter tahun dari config."""
    results = []
    
    # Detik search date params: tgl_mulai=01/01/2020&tgl_akhir=31/12/2026
    start_date = f"01/01/{config.START_YEAR}"
    end_date = f"31/12/{config.END_YEAR}"
    
    for page in range(1, config.PAGES_PER_KEYWORD + 1):
        params = {
            'query': keyword,
            'sortby': 'time',
            'page': page,
            'tgl_mulai': start_date,
            'tgl_akhir': end_date
        }
        
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get("https://www.detik.com/search/searchall", params=params, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.select('.list-content__item')
            
            if not articles: break
                
            for article in articles:
                title_elem = article.select_one('.media__title a')
                if title_elem:
                    url = title_elem['href']
                    judul = title_elem.get_text(strip=True)
                    
                    if url in seen_urls or judul.lower() in seen_titles:
                        continue
                    
                    # Ambil konten
                    content = get_full_content(url)
                    if content:
                        results.append({
                            'judul': judul,
                            'tanggal': datetime.now().strftime("%d %B %Y"),
                            'isi': content,
                            'sumber': 'detik',
                            'url': url
                        })
                        seen_urls.add(url)
                        seen_titles.add(judul.lower())
        except:
            break
    return results

def load_keywords(filepath):
    keywords = []
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                clean_kw = line.strip().strip("',").strip()
                if clean_kw: keywords.append(clean_kw)
    return keywords

def load_existing_data(dataset_file):
    """Memuat data yang sudah ada untuk pengecekan duplikat."""
    seen_urls = set()
    seen_titles = set()
    if os.path.exists(dataset_file):
        try:
            df = pd.read_csv(dataset_file)
            seen_urls = set(df['url'].astype(str).tolist())
            seen_titles = set(df['judul'].astype(str).str.lower().tolist())
        except:
            pass
    return seen_titles, seen_urls

if __name__ == "__main__":
    keywords = load_keywords(config.KEYWORDS_FILE)
    if not keywords: keywords = ["UMKM"]
    
    print(f"=== SCRAPER BERITA MULTI-SUMBER ({config.START_YEAR}-{config.END_YEAR}) ===")
    
    # 1. Load data lama
    seen_titles, seen_urls = load_existing_data(config.DATASET_FILE)
    print(f"Memuat {len(seen_titles)} data dari dataset.csv untuk menghindari duplikat.")

    all_new_data = []

    # 2. Proses RSS
    rss_data = scrape_rss(keywords, seen_titles, seen_urls)
    all_new_data.extend(rss_data)
    
    # 3. Proses Detik Search dengan Progress Bar
    print(f"\n[2/2] Mencari di Detik Search ({len(keywords)} Kata Kunci)...")
    pbar = tqdm(keywords, desc="Processing Keywords")
    
    for kw in pbar:
        pbar.set_description(f"Searching: {kw}")
        new_items = scrape_detik_search(kw, seen_titles, seen_urls)
        all_new_data.extend(new_items)
        if new_items:
            pbar.set_postfix(found=len(all_new_data))

    # 4. Simpan Hasil
    if all_new_data:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        temp_file = f"hasil_scrapping_{timestamp}.csv"
        
        # Simpan arsip
        pd.DataFrame(all_new_data).to_csv(temp_file, index=False, quoting=csv.QUOTE_ALL)
        
        # Update dataset
        if os.path.exists(config.DATASET_FILE):
            existing_df = pd.read_csv(config.DATASET_FILE)
            final_df = pd.concat([existing_df, pd.DataFrame(all_new_data)], ignore_index=True)
        else:
            final_df = pd.DataFrame(all_new_data)
        
        final_df.drop_duplicates(subset=['judul'], keep='first', inplace=True)
        final_df.to_csv(config.DATASET_FILE, index=False, quoting=csv.QUOTE_ALL)
        
        print(f"\nSelesai! Berhasil menambah {len(all_new_data)} berita baru.")
        print(f"Total di dataset.csv: {len(final_df)} berita.")
    else:
        print("\nTidak ada berita baru yang ditemukan.")
