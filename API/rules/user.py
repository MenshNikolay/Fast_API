from API.serializer import ShowUser
from API.serializer  import UserCreate
from db.layer import UserDAL


from hash import HashMaker


async def _create_new_user(body: UserCreate, session) -> ShowUser:
    async with session.begin():
        user_dal = UserDAL(session)
        user = await user_dal.create_user(
            name=body.name,
            surname=body.surname,
            email=body.email,
            hashed_password=HashMaker.get_password_hash(body.password),
        )
        return ShowUser(
            id=user.id,
            name=user.username,
            surname=user.usersurname,
            email=user.email,
            is_active=user.is_active,
        )