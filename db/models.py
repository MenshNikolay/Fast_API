# models.py
import datetime
from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True) 
    username = Column(String, index=True)
    usersurname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    sallary_usd = Column(Float, index=True, default=300.00)
    next_sallary_raise = Column(Date, index=True, default=datetime.date.today() + datetime.timedelta(days=180)) #need to be configurated in auto mode. change value every 180 days
    is_active = Column(Boolean(), default=True)
    hashed_password = Column(String, nullable=False)
