from src.repos.hotel import HotelRepository
from src.repos.room import RoomRepository
from src.repos.user import UserRepository



class DBManager:
    def __init__(self):
        self.session_factory = self.session_factory


    async def __aenter__(self):
        self.session = self.session_factory()

        self.hotel = HotelRepository(self.session)
        self.room = RoomRepository(self.session)
        self.user = UserRepository(self.session)

        return self


    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()


    async def commit(self):
        await self.session.commit()