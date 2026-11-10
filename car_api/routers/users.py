from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, exists

from car_api.models import User
from car_api.core.database import get_session
from car_api.core.security import get_password_hash
from car_api.db import USERS
from car_api.schemas.users import (
    UserListPublicSchema,
    UserSchema,
    UserPublicSchema
)

router = APIRouter()


@router.post(path='/', status_code=status.HTTP_201_CREATED, response_model=UserPublicSchema,
             summary='Criar novo usuário')
async def creater_user(user: UserSchema, db: AsyncSession = Depends(get_session)):
    username_exists = await db.scalar(select(exists().where(User.username == user.username)))
    email_exists = await db.scalar(select(exists().where(User.email == user.email)))

    if username_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='username já está em uso')

    if email_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='email já cadastrado')

    db_user = User(username=user.username, email=user.email, password=get_password_hash(user.password))
    db.add(db_user)


    await db.commit()


    await db.refresh(db_user)

    return db_user


@router.get(path='/', status_code=status.HTTP_200_OK, response_model=UserListPublicSchema)
async def list_user():
    return {'users': USERS}


@router.put(path='/{user_id}', status_code=status.HTTP_201_CREATED, response_model=UserPublicSchema)
async def update_user(user_id: int, user: UserSchema):
    user_with_id = UserPublicSchema(**user.model_dump(), id=user_id)
    USERS[user_id - 1] = user_with_id
    return user_with_id


@router.delete(path='/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    del USERS[user_id - 1]
    return
