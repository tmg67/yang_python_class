import requests
from bs4 import BeautifulSoup

#URL of a news website(example: BBC news)
url = "https://www.bbc.com/news"

#send GET request to the URL
response =  requests.get(url)
#print(response.text)
#check if the request was successful
if response.status_code == 200:
    print("page fetched successfully!\n")
    #parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    #find headlines(examples: find all <h3> tags with class 'gs-c-promo-heading__title')
    headlines = soup.find_all('h2', class_='sc-8ea7699c-3')
    #print(headlines)
    #display the firts 5 healines
    print("top 5 headlines:")
    for i, headline in enumerate(headlines[:5]):
        print(f"{i + 1}. {headline.get_text()}")
else:
    print(f"failed to retrived data. status code: {response.status_code}")
