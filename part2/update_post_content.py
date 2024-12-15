from database import SessionLocal
from models import Post

def update_post_content(post_id, new_content):
    session = SessionLocal()
    try:
        post = session.query(Post).filter(Post.id == post_id).first()
        if not post:
            print(f"Пост с ID {post_id} не найден.")
            return
        post.content = new_content
        session.commit()
        print(f"Содержимое поста ID {post_id} обновлено.")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при обновлении поста: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    update_post_content(1, 'Новое содержимое первого поста Джона.')
