from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.utils.hash import verify_password
from app.core.token import create_access_token
from app.services.user_service import get_user_by_email

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
