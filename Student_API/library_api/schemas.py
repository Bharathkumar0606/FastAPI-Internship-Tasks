
from pydantic import BaseModel, EmailStr
from datetime import date


# -----------------------------
# Book Schemas
# -----------------------------

class BookBase(BaseModel):
    title: str
    author: str
    available_copies: int


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True


# -----------------------------
# Member Schemas
# -----------------------------

class MemberBase(BaseModel):
    name: str
    email: EmailStr


class MemberCreate(MemberBase):
    pass


class MemberResponse(MemberBase):
    id: int

    class Config:
        from_attributes = True


# -----------------------------
# Borrow Schemas
# -----------------------------

class BorrowCreate(BaseModel):
    member_id: int
    book_id: int


class BorrowResponse(BaseModel):
    id: int
    member_id: int
    book_id: int
    borrow_date: date
    return_date: date | None = None

    class Config:
        from_attributes = True
