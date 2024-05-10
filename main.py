from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.routing import APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from datetime import datetime, timedelta
from pydantic import BaseModel
import jwt
import uvicorn
from API.create_user_handler import user_router
from API.login_user_hadler import login_router
import asyncio


app = FastAPI(title="shift-project")
security = HTTPBasic()


main_api_router = APIRouter()

main_api_router.include_router(login_router, prefix="/login", tags=["login"])
#main_api_router.include_router(login_router, prefix="/userinfo", tags=["sallary"])
main_api_router.include_router(user_router, prefix="/user", tags=["user"])


app.include_router(main_api_router)








