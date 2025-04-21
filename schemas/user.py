
import bcrypt
from pydantic import BaseModel, EmailStr, field_validator


class UserPydantic(BaseModel):
    username: str
    password: bytes
    email: EmailStr

        
    
    @field_validator('password', mode='before')
    @classmethod
    def password_change(cls, value):
        if not isinstance(value, bytes):
            return bcrypt.hashpw(value, bcrypt.gensalt()) 
        return value
        
        