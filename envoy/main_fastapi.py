from typing import Optional
from fastapi import FastAPI, Request, Response
from uvicorn.protocols.utils import get_client_addr, get_local_addr
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World App"}


@app.get("/items/{item_id}")
def read_item(item_id: int, request: Request, response: Response):
    print("---",get_client_addr.__dir__())
    print("local addre",get_local_addr.__dir__())
    return {"item_id": item_id, "client_host": request.client}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)