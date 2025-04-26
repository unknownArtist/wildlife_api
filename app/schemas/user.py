from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False


class UserCreate(UserBase):
    email: EmailStr
    username: str
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None
    created_date: Optional[date] = None
    last_login: Optional[date] = None

    class Config:
        orm_mode = True
        from_attributes = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    hashed_password: str 