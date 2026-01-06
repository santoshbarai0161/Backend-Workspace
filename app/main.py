from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app=FastAPI()

class Post(BaseModel):
    title:str
    content:str

@app.get("/")
def root():
	return "Hello World"
@app.get("/posts")
def get_posts():
    return {"data":"Here is all of your post"}
@app.post("/createpost")    #testing post 
def create_post(post:Post):
    print(post.model_dump())
    return {'data':post}
