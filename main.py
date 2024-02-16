from typing import Union
from fastapi import Request
import uvicorn
from fastapi import FastAPI
import requests

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

@app.get("/ping")
def main(request: Request):
    for url in list_of_nodes:
        try:
            requests.head('http://'+url+':8000/')
        except requests.exceptions.ConnectionError:
            list_of_nodes.remove(url)

if __name__ == '__main__':
    uvicorn.run(app,host='100.73.159.142',port=8001)
