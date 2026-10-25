from fastapi import FastAPI

app = FastAPI()

# GET: this only calculates and returns a result, nothing is saved or changed
@app.get("/add")
def add(a: int, b: int):
    # int type hints make FastAPI convert the query strings to integers
    return {"sum": a + b}