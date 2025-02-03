# 🔹 Task: Make a book library manager that stores books in SQLite.
# Use SQLAlchemy to add, remove, and search for books.
# Query books by genre, author, or rating

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

Base = declarative_base()

class Library(Base):
    __tablename__ = 'library'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_product = Library(name='Science', price=299.99)
new_product = Library(name='Maths', price=3000)

session.add(new_product)
session.commit()
for library in session.query(Library):
    print(library.name, library.price)
