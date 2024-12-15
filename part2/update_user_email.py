from database import SessionLocal
from models import User

def update_user_email(username, new_email):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if not user:
            print(f"Пользователь с именем {username} не найден.")
            return
        user.email = new_email
        session.commit()
        print(f"Email пользователя {username} обновлен на {new_email}.")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при обновлении email пользователя: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    update_user_email('john_doe', 'john_new@example.com')
