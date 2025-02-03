# 📌 Task: Movie & TV Show Recommendation System
# 🌟 Objective:
# Create a Python application that recommends movies or TV shows to users based on their preferences, using NumPy, Pandas, CSV, SQLite, Requests, and Matplotlib.

# 🔧 Concepts Covered:
# ✅ requests - Fetch movie/TV show data from an API (e.g., TMDB API).
#  ✅ sqlite3 - Store and manage movie/show data in a local database.
#  ✅ pandas - Process and analyze user preferences.
#  ✅ numpy - Perform similarity calculations for recommendations.
#  ✅ csv - Export user history and recommendations.
#  ✅ matplotlib - Visualize movie trends and ratings.

# 📝 Task Breakdown:
# 1️⃣ Fetch Movie/TV Show Data (Using requests)
# Use the TMDB API (https://www.themoviedb.org/) to get data on:
#  ✅ Movie/show title
#  ✅ Genre
#  ✅ Ratings
#  ✅ Release date
# 2️⃣ Store Data in SQLite (Using sqlite3)
# # Save user preferences and watched history in a database (movies.db).
# 3️⃣ Process & Analyze Data (Using pandas & numpy)
# Load data into a Pandas DataFrame for analysis.
# Implement a recommendation algorithm based on:
#  ✅ Genre similarity (users who like sci-fi get sci-fi recommendations).
#  ✅ Average ratings (highly rated movies recommended first).
#  ✅ Recent releases (prioritize new movies).
# 4️⃣ Export Data to CSV (Using csv & pandas)
# Save recommended movies to recommendations.csv.
# 5️⃣ Visualize Movie Trends (Using matplotlib)
# Bar chart: Show top 5 genres the user watches most.
# Pie chart: Show percentage of ratings (e.g., how many 5-star movies).
# # Line graph: Show trend of movie releases per year.

import requests

url = "https://www.freetestapi.com/api/v1/movies"

response = requests.get(url)
if response.status_code == 200:
    print("data fetched succesfully")

    data = response.json()

    for post in data [:4]:
        print(f"Post Title: {post['title']}")
        print(f"Genre: {post['genre']}")
        print(f"Rating: {post['rating']}")
        print(f" Year: {post['year']}")
else:
    print(f"failed to retrieve data. Status code:{response.status_code}")
import sqlite3
from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movie"
    title = Column(String, nullable=False)
    rating = Column(Float, nullable= False)
    genre = Column(String, nullable=False)
    year = Column(Float, nullable=False)

engine = create_engine('sqlite:///movie.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_product = Movie(title="The Godfather", genre="'Crime', 'Drama'",rating=9.2, year=1972)
new_product = Movie(title="The Dark Knight", genre="'Action', 'Crime', 'Drama'", rating=9, year=2008)

session.add(new_product)
session.commit()
for movie in session.query(Movie):
    print(movie.name, movie.price)
