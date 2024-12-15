from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import User, Post
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from fastapi.templating import Jinja2Templates
from database import get_db

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/users", response_class=HTMLResponse)
def read_users(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.post("/users")
def create_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    new_user = User(username=username, email=email, password=password)
    try:
        db.add(new_user)
        db.commit()
        return RedirectResponse(url="/users", status_code=303)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="User with this username or email already exists")


@app.get("/users/edit/{user_id}", response_class=HTMLResponse)
def edit_user(request: Request, user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("edit_user.html", {"request": request, "user": user})


@app.post("/users/update/{user_id}")
def update_user(
    user_id: int,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(None),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.username = username
    user.email = email
    if password:  # Обновление пароля только если оно предоставлено
        user.password = password
    db.commit()
    return RedirectResponse(url="/users", status_code=303)


@app.post("/users/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return RedirectResponse(url="/users", status_code=303)


# --- Posts ---
@app.get("/posts", response_class=HTMLResponse)
def read_posts(request: Request, db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return templates.TemplateResponse("posts.html", {"request": request, "posts": posts})


@app.post("/posts")
def create_post(
    title: str = Form(...),
    content: str = Form(...),
    user_id: int = Form(...),
    db: Session = Depends(get_db),
):
    if not db.query(User).filter(User.id == user_id).first():
        raise HTTPException(status_code=400, detail="User does not exist")
    new_post = Post(title=title, content=content, user_id=user_id)
    db.add(new_post)
    db.commit()
    return RedirectResponse(url="/posts", status_code=303)


@app.get("/posts/edit/{post_id}", response_class=HTMLResponse)
def edit_post(request: Request, post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return templates.TemplateResponse("edit_post.html", {"request": request, "post": post})


@app.post("/posts/update/{post_id}")
def update_post(
    post_id: int,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db),
):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post.title = title
    post.content = content
    db.commit()
    return RedirectResponse(url="/posts", status_code=303)


@app.post("/posts/delete/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return RedirectResponse(url="/posts", status_code=303)