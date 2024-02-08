from typing import Union
from fastapi import Request
import uvicorn
from fastapi import FastAPI

app = FastAPI()

list_of_nodes = []


@app.post("/")
async def main(request: Request):
    data = await request.json()
    if data['host'] not in list_of_nodes:
        list_of_nodes.append(data['host'])

@app.get("/")
async def main(request: Request):
    return {
        'hosts': list_of_nodes,
    }

if __name__ == '__main__':
    uvicorn.run(app,port=80)