#fastapi allows you to delcare additional information and validation for your parameters. 
from typing import Annotated
from fastapi import FastAPI
app = FastAPI()

# @app.get("/items")
# async def read_items(q:str | None = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id":"bar"}]}
#     if q:
#         results.update({"q":q})
#     return results

#We are going to enforce that even though q is optional, whenever it is provided, its length doesn't exceed 50 characters.

@app.get("/items")
async def read_items(q: Annotated)
    