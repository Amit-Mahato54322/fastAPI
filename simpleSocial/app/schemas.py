# request body
# define the type of data that we are gonna accept in post
from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str