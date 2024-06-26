from typing import Generator


from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

#rout to db
DATABASE_URL = "postgresql+asyncpg://postgres:361629Qaz@localhost/fastapi"
#interaction with db
engine = create_async_engine(DATABASE_URL, future=True, echo=True)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db()-> Generator:
    try: 
        session: AsyncSession = async_session()
        yield session 
    finally:
        await session.close()    
