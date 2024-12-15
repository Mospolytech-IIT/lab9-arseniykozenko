from database import SessionLocal
from models import User

def add_users():
    session = SessionLocal()
    try:
        users = [
            User(username='arseniy_kozenko', email='arseniy@gmail.com', password='arseniy123'),
            User(username='nikita_azarov', email='nikita@gmail.com', password='nikita321'),
            User(username='sergey_voronin', email='sergey@gmail.com', password='serg456')
        ]
        session.add_all(users)
        session.commit()
        print("Пользователи добавлены успешно.")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении пользователей: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    add_users()
