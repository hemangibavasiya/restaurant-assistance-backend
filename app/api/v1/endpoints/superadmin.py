from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models.superadmin import SuperAdmin
from app.api.v1.schemas import SuperAdminCreate, SuperAdminResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/superadmin/login", response_model=SuperAdminResponse)
def login_superadmin(email: str, password: str, db: Session = Depends(get_db)):
    admin = db.query(SuperAdmin).filter(SuperAdmin.email == email).first()
    if not admin:
        raise HTTPException(status_code=404, detail="SuperAdmin not found")
    # Password verification logic (hash compare)
    return admin

@router.post("/superadmin/add/restaurants")
def register_restaurant(...):
    # Implementation for adding restaurants
    pass
