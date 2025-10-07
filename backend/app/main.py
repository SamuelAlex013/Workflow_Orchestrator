# main entry point for the FastAPI application
from fastapi import FastAPI

app = FastAPI()

# default starter route for fastapi
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# To run the application, use the command:
# uvicorn main:app --reload
