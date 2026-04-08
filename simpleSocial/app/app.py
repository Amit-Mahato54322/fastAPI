from fastapi import FastAPI

app = FastAPI()

text_post = {1: {"title": "New post", "Content": "cool test post"}}

@app.get("/posts")
def get_all_posts():
    return text_post

@app.get("/posts/{id}")
def get_post(id:int):
    return text_post.get(id)