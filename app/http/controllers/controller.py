from app.entity.user import User

class Controller():
    async def index():
        return {
            'id': 1,
            'item': [1,2,3,4,5,6]
        }
    
    async def store(user_id: str):
        """
        asdasdasd asdas d as
        """
        return await User.filter(username="asdasdas").all()
    
class UserController:
    async def index(user: str):
        return {
            "user": user
        }