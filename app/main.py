from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Author": "63102230 Chitsanupong Paenyoi"}

@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.post("/callname")
def post_name(name: str = None):
    return {"hello": name}

handler = Mangum(app)
