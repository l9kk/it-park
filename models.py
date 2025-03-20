from pydantic import BaseModel, EmailStr, Field, field_validator
import re
from typing import Optional


class ContactForm(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="User's first name")
    surname: str = Field(..., min_length=1, max_length=50, description="User's last name")
    phone: str = Field(..., description="User's phone number")
    email: EmailStr = Field(..., description="User's email address")
    message: str = Field(..., min_length=1, max_length=1000, description="User's message or feedback")

    @field_validator('phone')
    def validate_phone(cls, v):
        if not re.match(r'^\+?[0-9\s\-\(\)]{8,20}$', v):
            raise ValueError('Invalid phone number format')
        return v


class ContactFormResponse(BaseModel):
    status: str
    message: str
    form_id: Optional[str] = None