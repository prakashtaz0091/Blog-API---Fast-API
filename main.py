from fastapi import FastAPI
from routes import blog_routes


app = FastAPI(
    title="Simple Blog API",
    description="This is a simple blog API made by using FastAPI for assignment",
    version="1.0.0"
)

# Include the blog routes too
app.include_router(blog_routes.router, prefix="/api", tags=["Blog"])

@app.get("/")
def root():
    return {"message": "Welcome to the Blog API made by using FastAPI!"}