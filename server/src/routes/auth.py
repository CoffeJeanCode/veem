from fastapi import APIRouter, Response, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.config.database import connection, get_db
from src.models.user import User
from src.schemas.user import UserAuth, User as UserSchema
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta

auth = APIRouter(prefix="/auth", tags=["Auth"])

SECRET_KEY = "ASDKLJASLKJ"
ALGORITHM = "HS256"

bcrypyt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login")

@auth.post("/login")
def login(user: UserAuth, db: Session = Depends(get_db)):
  user = user.dict()

  user = authenticate_user(user["email"], user["password"], db)
  
  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail=f"Could not validate user"
    )

  token = create_access_token(user.email, user.user_id, timedelta(minutes=60 * 48))

  return {"token": token, "token_type": "bearer" }

def authenticate_user(email: str, password: str, db: Session):
  user = db.query(User).filter(User.email == email).first()

  if not user:
    return False
  
  if not bcrypyt_context.verify(password, user.password):
    return False
  
  return user

def create_access_token(email: str, user_id: int, expires_delta: timedelta):
  encode = {"sub": email, "id": user_id}
  expires = datetime.utcnow() + expires_delta

  encode.update({"exp": expires})

  return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)