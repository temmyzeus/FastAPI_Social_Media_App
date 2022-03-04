import logging
import os
import time
from typing import Optional

import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

api = FastAPI(title="Social Media App")
logging.basicConfig(filename="logs/api.log", filemode="w", level=logging.INFO)

# Implement CRUD
posts: list[dict[str]] = [
    {
        "id": 1,
        "Title": "The Bad Fruit is rotten",
        "content": "Bla Bla Bla",
        "published": True,
    },
    {
        "id": 2,
        "Title": "The Golden Crown",
        "content": "Blu Blu Blu",
        "published": False,
    },
    {
        "id": 3,
        "Title": "Finders & Keepers",
        "content": "Ble Ble Ble",
        "published": True,
    },
]

# Read Env variables from .env file
dotenv.load_dotenv()

# Connect to Database
while True:
    try:
        conn = psycopg2.connect(
            database=os.environ["DATABASE"],
            user=os.environ["DATABASE_USER"],
            password=os.environ["DATABASE_PASSWORD"],
            host=os.environ["DATABASE_HOST"],
            port=os.environ["DATABASE_PORT"],
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        logging.info("Database Connection Successful")
        break
    except Exception as e:
        logging.error("Database Connection Failed!!")
        time.sleep(2)


class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = 1


@api.get("/")
def root():
    return "Social Media App with Fast API"


@api.get("/posts")
def get_posts():
    """Get a post with specified ID from DataBase"""
    cursor.execute("SELECT * FROM Posts")
    posts = cursor.fetchall()
    # return this output as json
    return posts


@api.get("/post/{id}")
def get_post(id: int):
    """Get all Posts from DataBase"""
    cursor.execute("SELECT * FROM Posts WHERE id=%s", vars=(id,))
    post = cursor.fetchone()
    if post:
        return post
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="ID not found in database!"
        )


@api.post("/post")
def create_post(post: Post):
    """Create post"""
    cursor.execute(
        "INSERT INTO Posts (title, content, published, rating) VALUES (%s, %s, %s, %s)",
        vars=(post.title, post.content, post.published, post.rating),
    )
    conn.commit()
    return {
        "detail": "New Post Created"
    }


@api.put("/post/{id}")
def update_post(id: int, post: Post):
    """Update Post in DataBase"""
    try:
        posts[id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} not found!"
        )
    else:
        posts[id] = post
        return {"detail": "Post Updated Successfully!"}


@api.delete("/post/{id}")
def delete_post(id: int):
    """Delete Post from DataBase"""
    # What to do if the id is not found in DB??
    cursor.execute("DELETE FROM Posts WHERE id=%s RETURNING *", vars=(id,))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post:
        return {
            "detail": f"Post {id} deleted from DataBase!"
            }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {id} not found in database",
        )
