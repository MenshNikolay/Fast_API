from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import constr
from pydantic import EmailStr
from pydantic import field_validator

class TunedModel(BaseModel):
    class Config:
        from_attributes = True


class ShowUser(TunedModel):
        id: int
        name: str
        surname: str
        email: EmailStr
        is_active: bool



class UserCreate(BaseModel):
        name: str
        surname: str
        email: EmailStr
        password: str

class Token(BaseModel):
    access_token: str
    token_type: str
              
 