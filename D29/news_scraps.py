import requests
from bs4 import BeautifulSoup

url = 'https://abcnews.go.com/Politics/live-updates/trump-second-term-live-updates/?id=118389757'
response = requests.get(url)

if response.status_code == 200:
    print("fetched successfully\n")
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('h2', class_= "PFoxV eBpQD rcQBv bQtjQ lQUdN GpQCA mAkiF FvMyr WvoqU nPLLM tuAKv ZfQkn GdxUi fPmhQ BXZNB ")

    print(headlines)
else:
    print(f"failed to retrived data. status code: {response.status_code}")
