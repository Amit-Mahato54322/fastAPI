from fastapi import FastAPI

app = FastAPI()

@app.get('/blog')
def index(limit:int, published:bool):
    if published == True:
        return {'data': f'{limit} published blogs from the database. '}
    else:
        return {"data": f"{limit} blogs from the database"}

