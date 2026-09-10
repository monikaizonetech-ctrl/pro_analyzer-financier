from app.core.database import SessionLocal
from app.models.core import User, RoleEnum
from app.core.security import get_password_hash

def seed_db():
    db = SessionLocal()
    
    # Check if admin already exists
    admin = db.query(User).filter(User.email == "admin@financier.com").first()
    if not admin:
        new_admin = User(
            email="admin@financier.com",
            hashed_password=get_password_hash("admin123"),
            name="System Administrator",
            role=RoleEnum.ADMIN
        )
        db.add(new_admin)
        db.commit()
        print("Admin user created successfully!")
    else:
        print("Admin user already exists.")
        
    db.close()

if __name__ == "__main__":
    seed_db()
