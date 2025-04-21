
class UserController:
    model = User
    
    @connection
    async def create(self, session: AsyncSession, **data):
        session.execute(select(model).where(model.username == data.get('username')))        
    