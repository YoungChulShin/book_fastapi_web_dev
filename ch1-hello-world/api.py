from fastapi import FastAPI

# fast api 인스턴스 변수
app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }