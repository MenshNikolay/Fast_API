from typing import Union

from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

import settings
from db.layer import UserDAL
from db.models import User
from db.db_config import get_db
from hash import HashMaker

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


async def find_user_email(email: str, session: AsyncSession):
    async with session.begin():
        user_dal = UserDAL(session)
        return await user_dal.get_user_by_email(
            email=email,
        )

async def auth_user(email:str, password:str, db: AsyncSession):
    user = await find_user_email(email=email, session=db)
    if user is None:
        return
    if not HashMaker.verify_password(password, user.hashed_password):
        return
    return user