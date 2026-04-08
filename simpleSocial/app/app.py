from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

text_post = posts = {
    1: {"title": "New post", "Content": "cool test post"},
    2: {"title": "Morning thoughts", "Content": "Starting the day with coffee and code"},
    3: {"title": "Study session", "Content": "Reviewed data structures today"},
    4: {"title": "Workout log", "Content": "Completed a 5km run"},
    5: {"title": "Tech update", "Content": "Exploring FastAPI and PostgreSQL"},
    6: {"title": "Project idea", "Content": "Building a task manager app"},
    7: {"title": "Debugging day", "Content": "Fixed bugs in my C++ project"},
    8: {"title": "Lecture notes", "Content": "Learned about pipelining in CPUs"},
    9: {"title": "Weekend vibes", "Content": "Relaxing with some music"},
    10: {"title": "Late night coding", "Content": "Pushing commits at 2 AM"}
}

@app.get("/posts")
def get_all_posts():
    return text_post

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_post:
        raise HTTPException(status_code=404, detail="post not found")
    return text_post.get(id)