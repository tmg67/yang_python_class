import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
#print(type(response.content))
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)
##### Extract quotes, authors, and tags
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

### print the extracted information
for quote, author, tag in zip(quotes, authors, tags):
    print(f'Quote: {quote.text}')
    print(f'Author: {author.text}')
    print('Tags:')
    for t in tag.find_all('a', class_=tags):
        print(f'- {t.text}')
    print()