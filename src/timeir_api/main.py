from fastapi import FastAPI


app = FastAPI()


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome To Unofficial Timeir API✨"}
