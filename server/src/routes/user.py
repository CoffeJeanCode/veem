from fastapi import APIRouter, Response, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.config.database import connection, get_db
from src.models.user import User
from src.schemas.user import UserCreate, User as UserSchema
from src.services.crypto import encrypt
from passlib.context import CryptContext


user = APIRouter(prefix="/user", tags=["Users"])
bcrypyt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@user.get("/")
async def get_all_users(db: Session = Depends(get_db)):
  try:
    all_users = db.query(User).all()
    return all_users
  except:
    return HTTPException()
    
@user.get("/{user_id}")
def get_one_user(user_id: str, db: Session=Depends(get_db)):
  user_found = db.query(User).filter(User.user_id == user_id ).first()
  
  if not user_found:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Not exist user with ID: {user_id}"
    )
  
  return  user_found

@user.post("/")
def create_user(user: UserCreate, db: Session=Depends(get_db)):
  user = user.dict()
  try:  
    user["password"] = bcrypyt_context.hash(user["password"].encode("utf-8"))

    new_user = User(username=user["username"], email=user["email"], password=user["password"])

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
  except Exception as error:
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail=f"Have been error with user creation"
    )

@user.delete("/{user_id}")
def delete_user(user_id: int, db: Session=Depends(get_db)):
  deleted_user = db.query(User).filter(User.user_id == user_id).first()
  
  if not deleted_user:
    raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail=f"Not exist user with ID: {user_id} for delete"
          )
  
  db.delete(deleted_user)
  db.commit()

  return Response(content="User have beend deleted")

  @user.put("/{user_id}")
  def update_user(user_id: int, updated_user: UserSchema, db: Session=Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    
    if not user:
      raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail=f"Not exist user with ID: {user_id}"
          )
    
    user.update(updated_user.dict( exclude_unset=True))
    db.commit()

    return {"respuesta":"Usuario actualizado correctamente!"}