from database import SessionLocal
from models import User

def delete_user(username):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if not user:
            print(f"Пользователь с именем {username} не найден.")
            return
        session.delete(user)
        session.commit()
        print(f"Пользователь {username} и все его посты удалены.")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при удалении пользователя: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    delete_user('jane_smith')
