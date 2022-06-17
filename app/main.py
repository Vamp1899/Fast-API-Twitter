from fastapi import FastAPI ,Response ,status ,HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Body
from typing import Optional , List
import utils
from random import randrange
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, get_db
from routers import post, user, auth, vote
#Used for CORS in Web
#fetch('http://localhost:8000 ').then(res => res.json()).then(console.log)
#This will generate table if we don't have alembic setted up from scratch
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from pydantic import BaseModel






#Only one function per URL
my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},
            {"title":"Fav foods","content":"I like pizza","id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i , p in enumerate(my_posts):
        if p['id'] == id:
            return i



#path route app are same thing
#app Decorator in this case converts it from simple function to API path operation

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def homepage():
    return {"message": "Hello Nikunj"}







