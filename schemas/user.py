from datetime import datetime
import string
from types import NoneType
from pydantic import BaseModel, ConfigDict, EmailStr, Field, ValidationError, field_validator

from enums import RoleEnum


class ProfilePD(BaseModel):
    phone: str | None = Field(None)
    name: str | None = Field(None)
    suname: str | None = Field(None)
    about: str | None = Field(None)
    date_birthday: datetime | None = Field(None)

    model_config = ConfigDict(from_attributes=True)


class UserPD(BaseModel):
    username: str = Field(..., min_length=6, max_length=16 )
    password: str|bytes = Field(..., min_length=8)
    email: EmailStr
    role: RoleEnum = Field(RoleEnum.DEMO)

    profile: dict = Field(None)

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    @field_validator('profile', mode='before')
    @classmethod
    def profile_to_dict(cls, value):
        
        if isinstance(value, dict):
            return dict(ProfilePD(**value))
        if isinstance(value, NoneType):
            return {}
        
        return dict(ProfilePD.model_validate(value))
    
    @field_validator('password')
    @classmethod
    def password_validate(cls, value):
        errors = []
        if isinstance(value, str):
            if not any(char.isdigit() for char in value):
                errors.append("Password must contain at least one digit.")
            if not any(char in string.punctuation for char in value):
                errors.append("Password must contain at least one punctuation mark.")
            if any(char not in string.ascii_letters for char in value if char.isalpha()):
                errors.append("Password must contain only english letters.")
        
        if errors:
            raise ValueError('\n• '.join(errors))
        
        return value

        

