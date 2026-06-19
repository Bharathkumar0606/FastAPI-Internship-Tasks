from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Student Model
class Student(BaseModel):
    id: int
    name: str
    email: EmailStr

# Course Model
class Course(BaseModel):
    id: int
    course_name: str

# Enrollment Model
class Enrollment(BaseModel):
    student_id: int
    course_id: int

# In-memory storage
students = []
courses = []
enrollments = []

# POST /students
@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student created successfully",
        "student": student
    }

# POST /courses
@app.post("/courses", status_code=status.HTTP_201_CREATED)
def create_course(course: Course):
    courses.append(course)
    return {
        "message": "Course created successfully",
        "course": course
    }

# POST /enroll
@app.post("/enroll", status_code=status.HTTP_201_CREATED)
def enroll_student(enrollment: Enrollment):

    student_exists = any(
        student.id == enrollment.student_id
        for student in students
    )

    course_exists = any(
        course.id == enrollment.course_id
        for course in courses
    )

    if not student_exists:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    if not course_exists:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    enrollments.append(enrollment)

    return {
        "message": "Enrollment successful"
    }

# GET /students/{id}/courses
@app.get("/students/{id}/courses")
def get_student_courses(id: int):

    student = next(
        (s for s in students if s.id == id),
        None
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    enrolled_course_ids = [
        enrollment.course_id
        for enrollment in enrollments
        if enrollment.student_id == id
    ]

    student_courses = [
        course
        for course in courses
        if course.id in enrolled_course_ids
    ]

    return {
        "student": student,
        "courses": student_courses
    }