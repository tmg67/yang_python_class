import requests
from bs4 import BeautifulSoup
import pandas as pd


NEPSE_URL = "https://merolagani.com/LatestMarket.aspx"


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


response = requests.get(NEPSE_URL, headers=HEADERS)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
   
    table = soup.find("table", {"class": "table"}) 
    
    headers = [th.text.strip() for th in table.find_all("th")]

   
    stock_data = []
    for row in table.find_all("tr")[1:]: 
        cols = row.find_all("td")
        if cols:
            company_name = cols[0].text.strip()
            stock_price = float(cols[1].text.strip().replace(",", ""))
            import_value = float(cols[5].text.strip().replace(",", ""))  
            stock_data.append([company_name, stock_price, import_value])
    
   
    df = pd.DataFrame(stock_data, columns=["Company", "Stock Price", "Import Value"])
    
 
    df.to_csv("nepse_data.csv", index=False)
    
    print("Nepse data successfully scraped and saved as nepse_data.csv!")

else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

#wheather forecast
LAT =27.7172 
LON =  85.3240

Weather_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current=temperature_2m,relative_humidity_2m,weathercode"


response = requests.get(Weather_URL)

if response.status_code == 200:
    data = response.json()
    
    current_weather = data["current"]
    temperature = current_weather["temperature_2m"]
    humidity = current_weather["relative_humidity_2m"]
    weather_code = current_weather["weathercode"] 
    
   
    print(f"Kathmandu Weather:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather Code: {weather_code}")
    
else:
    print(f"Failed to fetch weather data. HTTP Status Code: {response.status_code}")
    
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

url = "https://api.api-ninjas.com/v1/quotes"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Raw API Response:", data)

    if isinstance(data, list) and len(data) > 0:
        data = data[0]  

    content = data.get("content") or data.get("text") or "No quote found"
    author = data.get("author") or data.get("by") or "Unknown"

    subject = "Quote of the Day"
    message = f'"{content}"\n\n— {author}'

    sender_email = "yangjitamang9@gmail.com"  
    sender_password = ""  
    receiver_email = "yangchutamang27@gmail.com"  

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
    

    

