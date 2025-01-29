from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Float, nullable=False)

#create engine and session
engine = create_engine('sqlite:///store.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#add a new product
new_books = Book (title = 'science', author='dev', price=299.99)
new_books = Book (title = 'candy', author='shyam', price=299.98)
new_books = Book (title = 'math', author='hari', price=299.97)

session.add(new_books)
session.commit()

#Query products
for product in session.query(Book):
    print(Book.title, Book.author, Book.price)
    book = session.query(Book).filter(id=2)
    if book:
        author:"ram"
        title: "sugar"
        session.commit()
session.close()