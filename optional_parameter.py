from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{items_id}")
async def reload_item(item_id: str, q:str | None = None):
    if q:
        return {"item_id":item_id, "q":q}
    return {"item_id":item_id}