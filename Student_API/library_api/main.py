from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from database import engine, get_db
from models import Base, Book, Member, BorrowRecord
from schemas import (
    BookCreate,
    BookResponse,
    MemberCreate,
    MemberResponse,
    BorrowCreate,
    BorrowResponse
)

app = FastAPI(title="Library Management System API")

# Create tables
Base.metadata.create_all(bind=engine)


# ==========================
# HOME
# ==========================

@app.get("/")
def home():
    return {"message": "Library Management API Running"}


# ==========================
# BOOK APIs
# ==========================

@app.post("/books", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):

    new_book = Book(
        title=book.title,
        author=book.author,
        available_copies=book.available_copies
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


@app.get("/books", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):

    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book_data: BookCreate,
    db: Session = Depends(get_db)
):

    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    book.title = book_data.title
    book.author = book_data.author
    book.available_copies = book_data.available_copies
 
    db.commit()
    db.refresh(book)

    return book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):

    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}


# ==========================
# MEMBER APIs
# ==========================

@app.post("/members", response_model=MemberResponse)
def create_member(
    member: MemberCreate,
    db: Session = Depends(get_db)
):

    new_member = Member(
        name=member.name,
        email=member.email
    )

    db.add(new_member)
    db.commit()
    db.refresh(new_member)

    return new_member


@app.get("/members", response_model=list[MemberResponse])
def get_members(db: Session = Depends(get_db)):
    return db.query(Member).all()


# ==========================
# BORROW BOOK
# ==========================

@app.post("/borrow", response_model=BorrowResponse)
def borrow_book(
    borrow: BorrowCreate,
    db: Session = Depends(get_db)
):

    member = db.query(Member).filter(
        Member.id == borrow.member_id
    ).first()

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    book = db.query(Book).filter(
        Book.id == borrow.book_id
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    if book.available_copies <= 0:
        raise HTTPException(
            status_code=400,
            detail="Book unavailable"
        )

    record = BorrowRecord(
        member_id=borrow.member_id,
        book_id=borrow.book_id,
        borrow_date=date.today()
    )

    book.available_copies -= 1

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


# ==========================
# RETURN BOOK
# ==========================

@app.put("/return/{borrow_id}")
def return_book(
    borrow_id: int,
    db: Session = Depends(get_db)
):

    record = db.query(BorrowRecord).filter(
        BorrowRecord.id == borrow_id
    ).first()

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Borrow record not found"
        )

    if record.return_date:
        raise HTTPException(
            status_code=400,
            detail="Book already returned"
        )

    record.return_date = date.today()

    book = db.query(Book).filter(
        Book.id == record.book_id
    ).first()

    book.available_copies += 1

    db.commit()

    return {
        "message": "Book returned successfully"
    }


# ==========================
# AVAILABLE BOOKS
# ==========================

@app.get("/available-books")
def available_books(
    db: Session = Depends(get_db)
):

    return db.query(Book).filter(
        Book.available_copies > 0
    ).all()


# ==========================
# SEARCH BOOKS
# ==========================

@app.get("/search")
def search_books(
    title: str = "",
    author: str = "",
    db: Session = Depends(get_db)
):

    return db.query(Book).filter(
        Book.title.ilike(f"%{title}%"),
        Book.author.ilike(f"%{author}%")
    ).all()


# ==========================
# BORROW HISTORY
# ==========================

@app.get("/borrow-history")
def borrow_history(
    db: Session = Depends(get_db)
):
    return db.query(BorrowRecord).all()
