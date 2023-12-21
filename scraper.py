import requests
from bs4 import BeautifulSoup

def get_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f'Error {response.status_code} while fetching {url}')
        return None

def parse_webpage(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def extract_data(soup):
    titles = soup.find_all('a', {'class': 'bookTitle'})[:10]
    extracted_data = []
    for title in titles:
        new_book = title.find('a').text.strip()
        extracted_data.append(new_book)

    with open('data.txt', 'w') as f:
        for item in extracted_data:
            f.write(f'{item}\n')

    return extracted_data

def main():
    url = 'https://books.toscrape.com/'  
    content = get_webpage(url)
    if content:
        soup = parse_webpage(content)
        data = extract_data(soup)
        #print(data)

if __name__ == '__main__':
    main()