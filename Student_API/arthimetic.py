from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
def calculate(a: int, b: int):
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b
    }   