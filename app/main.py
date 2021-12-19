from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.vote import vote
from .database import engine
from .routers import post, user, auth, vote
from .import models
from .config import settings


#models.Base.metadata.create_all(bind=engine)

app=FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#my_posts = [{"title":"title of post 1", "content":"this is content of post 1", "id": 1}, {"title":"favourite food", "content":"i like pizza", "id": 2}]



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hi There, Welcome to my world, Good to see u Duh!!"}
