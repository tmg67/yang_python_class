import requests

#Github API URL for trending repositories (Python as an example)
url = "https://api.github.com/search/repositories?q=language:python&sort=start&order=decs"

#Send GET request to the Github API
response = requests.get(url)

#Check if the request was successful
if response.status_code == 200:
    print("Trending Respositories fetched successfully!\n")
    #Parse the JSON response
    data = response.json()

    #display the top 5 trending respotories
    for repo in data ['items'][:5]:
        name = repo['name']
        owner = repo['owner']['login']
        description = repo.get('description', 'no description available')
        stars = repo['stargazers_count']
        print(f"Repo Name: {name}\nOwner: {owner}\nStars: {stars}\nDescription: {description}\n")
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")