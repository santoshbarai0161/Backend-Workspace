from fastapi import FastAPI
from fastapi.params import Body
app=FastAPI()
@app.get("/")
def root():
	return "Hello World"
@app.get("/posts")
def get_posts():
    return {"data":"Here is all of your post"}
@app.post("/createpost")    #testing post 
def create_post(payload:dict=Body(...)):
    print(payload)
    return {"new post":f"title:{payload["title"]} and content: {payload['content']}"}
