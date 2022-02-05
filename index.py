from typing  import Optional
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def read_root():
    return("Welcome to the Book Store")


@app.get("/books/{book_id}")
def read_item(book_id: int, q: Optional[str] = None):
    return {"book_id": book_id, "q": q}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}