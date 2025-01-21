import requests

url = "https://www.weatherapi.com/weather/"

response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    data = response.header()

    weather_info = data.get("weather", {})
    location_info = data.get("location", {})
    date_info = data.get("date", {})

    print(f"enter your country name\n")
    print(f"enter your current location \n")
    print(f"enter date of today\n")

  
    print(f"Country: {weather_info.get['country']}")
    print(f"Location: {location_info.get['location']}")
    print(f"Date: {date_info.get['date']}\n")
    
else:
    print(f"Failed to retrieve data. Status Code:{response.status_code}")