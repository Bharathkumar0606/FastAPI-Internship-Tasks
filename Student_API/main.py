from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    email: EmailStr
    branch: str

students = []

@app.get("/students", response_model=List[Student])
def get_students():
    return students

@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student added successfully",
        "student": student
    }

