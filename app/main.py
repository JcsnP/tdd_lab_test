from fastapi import FastAPI, Body
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/callname")
def post_name(name: str = Body(...):
    if name is None:
        return {"warning": "name is None"}
    return {"hello": name}

@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": name}

handler = Mangum(app)
