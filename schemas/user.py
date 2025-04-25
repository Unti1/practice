from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, field_validator

from enums import RoleEnum


class ProfilePD(BaseModel):
    phone: str | None
    name: str | None
    suname: str | None
    about: str | None
    date_birthday: datetime | None

    model_config = ConfigDict(from_attributes=True)


class UserPD(BaseModel):
    username: str
    password: str|bytes
    email: EmailStr
    role: RoleEnum

    profile: dict

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    @field_validator('profile', mode='before')
    @classmethod
    def profile_to_dict(cls, value):
        
        if isinstance(value, dict):
            return dict(ProfilePD(**value))
        
        return dict(ProfilePD.model_validate(value))
    