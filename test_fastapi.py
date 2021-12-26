import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/")
async def root():
    return PlainTextResponse("Hello, World!")


if __name__ == '__main__':
    uvicorn.run("test_fastapi:app", port=5001, log_level="warning", workers=7)
