from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user, auth, blog, like, comment


app = FastAPI()
router = APIRouter()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(like.router)
app.include_router(comment.router)


# Middleware for handling CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


# Root endpoint, returns the index.html or any file you want to serve (no frontend folder now)
@app.get("/")
def root():
    return {"message": "Welcome to BLOG API"}
