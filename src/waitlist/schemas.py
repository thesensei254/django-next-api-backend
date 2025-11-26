from datetime import datetime
from ninja import Schema
from pydantic import EmailStr


class WaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email: EmailStr


class WaitlistEntryDetailSchema(Schema):
    # Create -> Data
    # WaitlistEntryOut
    email: EmailStr
    timestamp: datetime
