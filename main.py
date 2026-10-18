from database import get_books, add_book, delete_book
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def answer():
    return {"Main page"}

@app.get("/books")
def read_books():
    return get_books()

@app.get("/hello")
def hello():
    return {"message": "Привет!"}

class Book(BaseModel):
    id: int
    title: str
    author: str

@app.post("/books")
def add_new_book(book: Book):
    books = get_books()

    for existing_book in books:
        if existing_book["id"] == book.id:
            raise HTTPException(
                status_code=409,
                detail="Ошибка! Книга с таким ID уже существует."
            )
        
    add_book(book)
    
    return {"message": "Книга успешно добавлена."}

@app.delete("/books/{book_id}")
def handle_delete_book(book_id: int):
    books = get_books()

    book_exists = False
    for exesting_book in books:
        if exesting_book["id"] == book_id:
            book_exists = True
            break
    
    if not book_exists:
        raise HTTPException(
            status_code=404,
            detail="Ошибка! Книга с такм ID не найдена"
        )
    
    delete_book()

    return {"message": "Книга успешно добавлена."}
