from datetime import datetime
from types import NoneType
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

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
    password: str|bytes = Field(..., min_length=8, max_length=32)
    email: EmailStr
    role: RoleEnum = Field(RoleEnum.DEMO)

    profile: dict

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    @field_validator('profile', mode='before')
    @classmethod
    def profile_to_dict(cls, value):
        
        if isinstance(value, dict):
            return dict(ProfilePD(**value))
        if isinstance(value, NoneType):
            return {}
        
        return dict(ProfilePD.model_validate(value))
    