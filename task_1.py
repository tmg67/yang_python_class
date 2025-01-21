import requests

def fetch_weather_data(city_name):
    """
    fetch weather data for a given city using the open meteo API
    """
    #base URL for the open meteo API
    base_url = "https://api.open-meteo.com/v1/forecast"

    #Fake latitude and longitude lookup for the example
    #in real application, you would use a geocoding service to get the coordinates for the city name
    city_coordinate = {
        "Berlin": {"latitude": 52.52, "longitude": 13.41},
        "London": {"latitude": 51.51, "longitude": -0.13},
        "Paris": {"latitude": 48.86, "longitude": 2.35},
        "Tokyo": {"latitude": 35.69, "longitude": 139.69},
        "New York": {"latitude": 40.71, "longitude": -74.01},
    }

    #check if the city exists in the pre-defined coordinates
    if city_name not in city_coordinate:
        print("error: city not found in the coordinate list. please add or use a geocoding API.")
        return 
    #get latitude and longitude for the city
    coordinate = city_coordinate[city_name]
    latitude = coordinate["latitude"]
    longitude = coordinate["longitude"]

    #parameters for the API request
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
    }

    try:
        #send a GET request to the API
        response = requests.get(base_url, params=params)
        response.raise_for_status() #raise an HTTPError for bad responses(4xx and 5xx)
        #parse the JSON response
        weather_data = response.json()

        #extarct required data
        if "current_weather" in weather_data:
            current_weather = weather_data["current_weather"]
            temperature = current_weather["temperature"]
            weather_description = current_weather["weather_code"]#weather description code(requires mapping)
            wind_speed = current_weather["windspeed"]

            #display the extract weather data details
            print(f"city: {city_name}")
            print(f"temperature: {temperature}°C")
            print(f"weather code: {weather_description} (refer to API documentation for description)")
            print(f"wind speed: {wind_speed} km/h")
        else:
            print("error: unable to retrieve current weather data.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occured; {http_err}")
    except requests.exceptions.ConnectionError:
        print("Network error : please check your internet connection")
    except Exception as e:
        print(f"an error occured: {e}")

#input: Accept city name from the user
city = input("enter city name: ")
fetch_weather_data(city)