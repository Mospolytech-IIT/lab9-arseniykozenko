from database import SessionLocal
from models import User, Post

def get_posts_by_username(username):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if not user:
            print(f"Пользователь с именем {username} не найден.")
            return
        posts = session.query(Post).filter(Post.user_id == user.id).all()
        print(f"Посты пользователя {username}:")
        for post in posts:
            print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}")
    except Exception as e:
        print(f"Ошибка при извлечении постов пользователя: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    get_posts_by_username('john_doe')
