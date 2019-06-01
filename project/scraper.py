import re
import unicodedata

from bs4 import BeautifulSoup
import requests


def clean_text(text):
    no_diacritic = unicodedata.normalize('NFKD', text) \
        .encode('ascii','ignore') \
        .decode('utf-8')
    cleaned = re.sub(r'\W+', ' ', no_diacritic)
    
    return cleaned


def extract_main_page_urls(soup):
    urls = []
    for li_tag in soup.find_all('li', {'class': 'nomargin restriction_18'}):
        for a_tag in li_tag.find_all('a'):
            url = a_tag.attrs['href']
            if url[:4] == 'http':
                urls.append(url)
    return urls


def extract_thread_urls(soup):
    urls = []
    for a_tag in soup.find_all('a', {'class': 'fsB fs1'}):
        url = a_tag.attrs['href']
        if url[:4] == 'http':
            urls.append(url)
    return urls


def extract_texts(soup):
    thread_text = soup.find('div',
                       {'class': 'thread-decription'}).get_text()
    thread_text = " ".join(thread_text.split())
    texts = [clean_text(thread_text)]
    for comment in soup.find_all('div', {'class': 'thread-comment-decription'}):
        comment_text = " ".join(comment.get_text().split())
        texts.append(clean_text(comment_text))
    
    return texts

def process_page(url, function):

    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    return function(soup)


if __name__ == "__main__":
    main_page = requests.get("http://forum.gazeta.pl/forum/0,0.html").text
    main_soup = BeautifulSoup(main_page, 'html.parser')

    categories_urls = extract_main_page_urls(main_soup)

    with open('output.txt', 'a') as f:
        for category_url in categories_urls:
            print("Processing:", category_url)
            try:
                thread_urls = process_page(category_url, extract_thread_urls)

                for thread_url in thread_urls:
                    try:
                        texts = process_page(thread_url, extract_texts)
                        f.write('\n'.join(texts) + '\n')
                        
                    except:
                        pass
            except:
                pass
