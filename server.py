from fastapi import FastAPI, HTTPException
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!"}

@app.get("/erro")
async def root():
    raise HTTPException(status_code=400, detail="Erro!")

handler = Mangum(app)
