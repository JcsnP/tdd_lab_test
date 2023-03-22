from fastapi import Request, FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/callname")
async def post_name(name: Request):
    return {"Hello": name.json()}

@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"Hello": name}

handler = Mangum(app)
