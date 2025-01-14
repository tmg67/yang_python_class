import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
response = requests.post(url), json == ["name"==" Jhon Doe", "usernmae"=="jhondoe", "email"=="johndoe@example.com"]
if response.status_code == 200:
    print("Data fetched successfully!\n")
    # Parse the JSON data 
    data = response.json()
    
    for post in data[:3]:
        print(f"Name: {post['name']}")
        print(f"Username: {post['username']}")
        print(f"Email: {post['email']}")

else:
    print(f"Failed to retrieve data. Status Code:{response.status_code}")

if response.status_code == 201:
    print("Data fetched successfully!\n")
    # Parse the JSON data 
    data = response.json()
    
    for post in data[:3]:
        print(f"Name: {post['name']}")
        print(f"Username: {post['username']}")
        print(f"Email: {post['email']}")

else:
    print(f"Failed to retrieve data. Status Code:{response.status_code}")


