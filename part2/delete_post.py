from database import SessionLocal
from models import Post

def delete_post(post_id):
    session = SessionLocal()
    try:
        post = session.query(Post).filter(Post.id == post_id).first()
        if not post:
            print(f"Пост с ID {post_id} не найден.")
            return
        session.delete(post)
        session.commit()
        print(f"Пост с ID {post_id} удален.")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при удалении поста: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    delete_post(2)
