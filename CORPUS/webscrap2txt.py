import requests
import time
import random
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright


# ---------- FONCTION: fallback Playwright améliorée ----------
def get_content_with_playwright(url, timeout=15):
    try:
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)  # Lancement visible pour débug
            context = browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            )
            page = context.new_page()
            page.goto(url, timeout=timeout * 1000)
            time.sleep(2)  # Pause pour chargement complet
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")  # Scroll bas de page
            time.sleep(1)
            content = page.content()
            browser.close()
            return content
    except Exception as e:
        print(f"[Playwright] Échec pour {url} : {e}")
        return None


# ---------- FONCTION: Scraper avec fallback ----------
def get_page_content(url, timeout=15):
    headers = {
        'User-Agent': random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0'
        ])
    }

    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
        if response.status_code == 200:
            return response.text
        elif response.status_code == 403:
            print(f"[403] Accès refusé - fallback Playwright pour {url}")
            return get_content_with_playwright(url, timeout)
        else:
            print(f"[{response.status_code}] Erreur HTTP pour {url}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"[!] Erreur réseau pour {url}: {e}")
        return get_content_with_playwright(url, timeout)


# ---------- FONCTION: Extraire texte HTML ----------
def extract_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
        element.decompose()
    text = soup.get_text(separator=' ', strip=True)
    return text


# ---------- FONCTION: Sauvegarde ----------
def save_text(content, url, output_dir):
    domain = urlparse(url).netloc.replace('www.', '').replace('.', '_')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{domain}_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# URL: {url}\n")
        f.write(f"# Date: {datetime.now()}\n\n")
        f.write(content)

    print(f"[✓] Sauvegardé dans: {filepath}")


# ---------- FONCTION PRINCIPALE ----------
def main():
    urls_file = "urls.txt"
    output_dir = "resultat_new"
    delay_min, delay_max = 1.0, 3.0

    if not os.path.isfile(urls_file):
        print(f"[!] Fichier introuvable: {urls_file}")
        return

    with open(urls_file, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]

    print(f"[*] {len(urls)} URLs à traiter")

    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] Scraping: {url}")
        html = get_page_content(url)
        if html:
            text = extract_text(html)
            save_text(text, url, output_dir)
        else:
            print(f"[!] Échec pour {url}")

        if i < len(urls):
            wait = random.uniform(delay_min, delay_max)
            time.sleep(wait)


if __name__ == "__main__":
    main()
