from pydantic import BaseModel, Field

# class BlogPost(BaseModel):
#     title: str
#     content: str
#     author: str

class BlogPost(BaseModel):
    title: str = Field(..., title="Title of the Blog Post", max_length=100, example="My First Blog Post")
    content: str = Field(..., title="Content of the Blog Post", min_length=10, example="This is the content of the blog post.")
    author: str = Field(..., title="Author of the Blog Post", example="John Doe")
