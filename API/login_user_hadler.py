from datetime import timedelta, datetime

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

import security
from API.rules.auth import auth_user
from API.serializer import Token
from db.db_config import get_db
from security import create_access_token
from jose import jwt, JWTError,ExpiredSignatureError
from security import SECRET_KEY, ALGORITHM

login_router = APIRouter()

@login_router.post("/token", response_model=Token)
async def login_jwt(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    user = await auth_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Cheak your password or username.")
    
    life_time = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    next_sallary_raise = user.next_sallary_raise.strftime("%Y-%m-%d")
    access_token = create_access_token(data={"sub":f"{user.username} {user.usersurname}",
                                            "sensitive_info":[user.sallary_usd, next_sallary_raise]}, 
                                            expires_delta=life_time)
    
    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")

@login_router.get("/userinfo")
async def get_user_info(token: str = Depends(oauth2_scheme)):
    try:
        decrypted_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        #username, usersurname = decrypted_token["sub"]
        sallary_usd, next_sallary_raise = decrypted_token["sensitive_info"]
        return {
            #"username": username,
            #"usersurname": usersurname,
            "sallary_usd": sallary_usd,
            "next_sallary_raise": next_sallary_raise
        }
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    