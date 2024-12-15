from database import SessionLocal
from models import User, Post

def add_posts():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        if not users:
            print("Нет пользователей для добавления постов.")
            return
        
        posts = [
            Post(title='Первый пост Арсения', content='Содержимое первого поста Арсения.', user_id=users[0].id),
            Post(title='Второй пост Арсения', content='Содержимое второго поста Арсения.', user_id=users[0].id),
            Post(title='Пост Никиты', content='Содержимое поста Никиты.', user_id=users[1].id),
            Post(title='Пост Сергея', content='Содержимое поста Сергея.', user_id=users[2].id)
        ]
        session.add_all(posts)
        session.commit()
        print("Посты добавлены успешно.")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении постов: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    add_posts()
