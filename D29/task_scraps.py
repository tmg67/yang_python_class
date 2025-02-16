import  requests
from  bs4 import BeautifulSoup

url = 'https://www.programiz.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


Cup = soup.find_all('a')
for i in Cup:
    print(i.get('href'))