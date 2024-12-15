from database import SessionLocal
from models import User

def get_all_users():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
    except Exception as e:
        print(f"Ошибка при извлечении пользователей: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    get_all_users()
