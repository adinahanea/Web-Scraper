import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import nltk

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

def extract_data(soup, filename):
    titles = soup.find_all('h2')
    extracted_data = [title.text for title in titles]


    with open(filename, 'a') as f:
        for item in extracted_data:
            f.write(f'{item}\n')
        
        f.write('\n')

    return extracted_data

#nltk.download('punkt')    

def count_occurences(filename, words):
    with open(filename, 'r') as f:
        text = f.read()
        tokens = nltk.word_tokenize(text)
        words_found = Counter(word.lower() for word in tokens if word.lower() in set(words))
    return words_found

def main():
    url = 'https://thehackernews.com/'
    filename = 'data.txt'
    words = ['hacker', 'hackers', 'attack', 'attacks', 'malware', 'attacker', 'password']
    content = get_webpage(url)

    if content:
        soup = parse_webpage(content)
        data = extract_data(soup, filename)
        #print(data)
        word_counts = count_occurences(filename, words)
        print(word_counts)


if __name__ == '__main__':
    main()