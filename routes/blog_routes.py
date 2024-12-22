from fastapi import APIRouter, HTTPException
from models.blog_model import BlogPost

router = APIRouter()

# In-memory Global state to keep track of blog posts
blog_posts = {}

@router.post("/posts/", status_code=201)
def create_post(post: BlogPost):
    print(post)
    if post.title in blog_posts:
        raise HTTPException(status_code=400, detail="A post with this title already exists.")
    blog_posts[post.title] = post
    return {"message": "Post created successfully", "post": post}


@router.get("/posts/", response_model=list[BlogPost])
def get_posts():
    return list(blog_posts.values())



@router.put("/posts/{title}")
def update_post(title: str, updated_post: BlogPost):
    if title not in blog_posts:
        raise HTTPException(status_code=404, detail="Post not found.")
    if title != updated_post.title and updated_post.title in blog_posts:
        raise HTTPException(status_code=400, detail="A post with the new title already exists.")
    blog_posts.pop(title)
    blog_posts[updated_post.title] = updated_post
    return {"message": "Post updated successfully", "post": updated_post}



@router.delete("/posts/{title}")
def delete_post(title: str):
    if title not in blog_posts:
        raise HTTPException(status_code=404, detail="Post not found.")
    del blog_posts[title]
    return {"message": "Post deleted successfully"}