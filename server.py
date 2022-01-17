from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/erro")
async def root():
    raise HTTPException(status_code=401, detail="Erro!")
