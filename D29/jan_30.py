# Customer Order Management System
# 💡 Concepts: SQLite database, API calls (e.g., fake e-commerce API), email automation, CSV handling.
# 🔹 Task:
# Store customer orders in an SQLite database (Product, Quantity, Price, Customer Email).
# Fetch product details from an API (e.g., Fake Store API: https://fakestoreapi.com/).
# Generate an order summary CSV file and store it.
# Send an email confirmation to the customer with order details.
# 🎯 Bonus:
# Add a feature where users can track order status via email.
# Implement CRUD operations (add, delete, update orders).

import requests

url = "https://fakestoreapi.com/products"


response = requests.get(url)

if response.status_code == 200:
    print("Data fetched successfully!\n")

    data = response.json()

    for post in data[:3]:
        print(f"Post ID: {post['id']}")
        print(f"Price: {post['price']}")
        print(f"Product: {post['product']}")
else:
    print(f"failed to retrieve data. Status code:{response.status_code}")