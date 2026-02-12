from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.db import get_db
from backend.models.user_db import UserDB
from backend.utils.security import get_admin_user

router = APIRouter()


@router.get("/users")
def get_all_users(
    admin=Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    users = db.query(UserDB).all()
    return users
