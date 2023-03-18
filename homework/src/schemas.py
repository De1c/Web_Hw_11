from datetime import date as birth_date

from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    name: str = Field(min_length=2, max_length=15)
    surname: str = Field(min_length=2, max_length=15)
    email: EmailStr
    phone: str = Field(min_length=6, max_length=16)
    birthday: birth_date
    additionally: str = Field(min_length=3, max_length=300)


class ResponseContact(BaseModel):
    id: int = 1
    name: str = "Yehor"
    surname: str = "Ss"
    email: EmailStr = "yehorss@gmail.com"
    phone: str = "+380000000000"
    birthday: birth_date = birth_date(year=2005, month=4, day=20)
    additionally: str = "My best friend"

    class Config:
        orm_mode = True