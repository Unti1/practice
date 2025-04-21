

class User(Base):
    username : Mapped[str]
    
    @connection
    @classmethod
    async def create(cls, session: AsyncSessio,**data):
        ...
        
