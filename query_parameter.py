from fastapi import FastAPI

app = FastAPI()

@app.get('/blog')
def index(limit:int, published:bool):
    if published == True:
        return {'data': f'{limit} published blogs from the database. '}
    else:
        return {"data": f"{limit} blogs from the database"}

@app.get("/items/{item_id}")
async def read_item(item_id:str, q:str|None = None, short: bool = False):
    item = {"item_id":item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update()