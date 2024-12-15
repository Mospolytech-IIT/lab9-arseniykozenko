from database import SessionLocal
from models import Post

def get_all_posts_with_users():
    session = SessionLocal()
    try:
        posts = session.query(Post).join(Post.user).all()
        for post in posts:
            print(f"Post ID: {post.id}, Title: {post.title}, Author: {post.user.username}")
    except Exception as e:
        print(f"Ошибка при извлечении постов: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    get_all_posts_with_users()
