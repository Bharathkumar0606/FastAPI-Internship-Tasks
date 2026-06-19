# FastAPI Internship Tasks

## Project Overview

This repository contains a collection of FastAPI projects completed as part of my backend development internship. The tasks progress from basic API development using in-memory data storage to advanced database-driven applications using PostgreSQL and SQLAlchemy.

## Technologies Used

* Python
* FastAPI
* Pydantic
* PostgreSQL
* SQLAlchemy
* Uvicorn
* REST APIs
* Swagger UI

---

# Task 1 – Student API

## Objective

Develop a simple FastAPI application to manage student records using in-memory storage.

## Features Implemented

* Create Student
* View All Students
* Input Validation using Pydantic
* Automatic API Documentation using Swagger

## APIs

| Method | Endpoint  | Description           |
| ------ | --------- | --------------------- |
| POST   | /students | Create a new student  |
| GET    | /students | Retrieve all students |

## Student Model

* id
* name
* email
* branch

## Concepts Learned

* FastAPI Fundamentals
* Pydantic Validation
* GET Requests
* POST Requests
* HTTP Status Codes
* API Documentation

---

# Task 2 – Product Management API

## Objective

Build a Product Management System implementing CRUD operations.

## Features Implemented

* Add Product
* View Products
* Update Product
* Delete Product
* Error Handling
* Input Validation

## APIs

| Method | Endpoint       | Description      |
| ------ | -------------- | ---------------- |
| POST   | /products      | Create product   |
| GET    | /products      | Get all products |
| PUT    | /products/{id} | Update product   |
| DELETE | /products/{id} | Delete product   |

## Product Model

* id
* name
* price
* quantity

## Concepts Learned

* CRUD Operations
* Path Parameters
* Request Body
* Response Models
* Data Validation
* REST API Design

---

# Task 3 – Student Course API

## Objective

Manage students, courses, and enrollments using FastAPI.

## Features Implemented

* Student Creation
* Course Creation
* Student Enrollment
* Retrieve Courses Enrolled by Student

## APIs

| Method | Endpoint               | Description              |
| ------ | ---------------------- | ------------------------ |
| POST   | /students              | Create student           |
| POST   | /courses               | Create course            |
| POST   | /enroll                | Enroll student in course |
| GET    | /students/{id}/courses | Get enrolled courses     |

## Models

### Student

* id
* name
* email

### Course

* id
* course_name

### Enrollment

* student_id
* course_id

## Concepts Learned

* One-to-Many Relationships
* Many-to-Many Relationships
* API Design Principles
* Nested Responses
* Data Validation
* Relationship Management

---

# Task 4 – Library Management System API

## Objective

Develop a Library Management System using FastAPI, PostgreSQL, and SQLAlchemy.

## Features Implemented

### Books Management

* Create Book
* View Books
* Update Book
* Delete Book

### Members Management

* Create Member
* View Members
* Update Member
* Delete Member

### Borrowing System

* Borrow Book
* Return Book
* View Borrow History
* Available Books Management

## Database Integration

* PostgreSQL Database
* SQLAlchemy ORM
* Table Relationships
* Persistent Data Storage

## Project Structure

library_api/

* database.py
* models.py
* schemas.py
* main.py

## Book Model

* id
* title
* author
* available_copies

## Member Model

* id
* name
* email

## Borrow Record Model

* id
* member_id
* book_id
* borrow_date
* return_date

## Concepts Learned

* FastAPI Architecture
* SQLAlchemy ORM
* PostgreSQL Integration
* Database Relationships
* Dependency Injection
* Exception Handling
* API Design Best Practices

---

# Additional Practice

## Arithmetic API

Created a simple FastAPI application to perform arithmetic operations.

### Operations

* Addition
* Subtraction
* Multiplication
* Division

### Concepts Learned

* Query Parameters
* User Input Handling
* API Responses
* FastAPI Route Creation

---

# Learning Outcomes

Through these projects, I gained practical experience in:

* FastAPI Development
* REST API Design
* Pydantic Validation
* CRUD Operations
* PostgreSQL Database Management
* SQLAlchemy ORM
* API Testing with Swagger UI
* Relationship Modeling
* Backend Development Best Practices

These tasks helped strengthen my understanding of backend application development and API architecture using Python and FastAPI.
