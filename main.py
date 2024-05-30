from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()


class ChatMessage(BaseModel):
    message: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/chat")
async def chat(msg: ChatMessage):
    try:
        print(msg.message)
        return JSONResponse(content={"message": msg.message})
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
