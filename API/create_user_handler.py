from logging import getLogger

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from API.serializer import UserCreate, ShowUser
from API.rules.user import _create_new_user

from db.models import User
from db.db_config import get_db

user_router = APIRouter()
logger = getLogger(__name__)


@user_router.post("/", response_model= ShowUser)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> ShowUser:
    try:
        return await _create_new_user(body, db)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")