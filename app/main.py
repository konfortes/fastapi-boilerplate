import uvicorn
from fastapi import FastAPI

from app.routers import items

app = FastAPI()

app.include_router(items.router)


@app.get("/health")
async def health():
    return {"status": "OK"}


# allow debugging
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
