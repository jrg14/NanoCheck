from hashlib import sha256
from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi import status
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.core.db import get_db
from backend.modules.users.models import User
from backend.modules.users.schemas import UserCreate
from backend.modules.users.schemas import UserRead
from backend.modules.users.schemas import UserUpdate


router = APIRouter(prefix="/users", tags=["users"])


def hash_password(password: str) -> str:
    return sha256(password.encode("utf-8")).hexdigest()


DbSession = Annotated[Session, Depends(get_db)]


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: DbSession) -> User:
    existing_user = db.scalar(select(User).where(User.email == payload.email))
    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with that email already exists.",
        )

    user = User(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(payload.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get("/", response_model=list[UserRead])
def list_users(db: DbSession) -> list[User]:
    return list(db.scalars(select(User).order_by(User.id)).all())


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: DbSession) -> User:
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )
    return user


@router.patch("/{user_id}", response_model=UserRead)
def update_user(user_id: int, payload: UserUpdate, db: DbSession) -> User:
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )

    updates = payload.model_dump(exclude_unset=True)

    if "email" in updates:
        existing_user = db.scalar(
            select(User).where(User.email == updates["email"], User.id != user_id)
        )
        if existing_user is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A user with that email already exists.",
            )

    if "name" in updates:
        user.name = updates["name"]
    if "email" in updates:
        user.email = updates["email"]
    if "password" in updates:
        user.password_hash = hash_password(updates["password"])

    db.commit()
    db.refresh(user)
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: DbSession) -> Response:
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )

    db.delete(user)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
