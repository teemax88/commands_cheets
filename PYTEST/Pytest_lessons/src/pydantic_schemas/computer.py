from pydantic import BaseModel, EmailStr
from pydantic.types import PastDate, FutureDate, PaymentCardNumber
from typing import List
from pydantic.networks import IPv4Address, IPv6Address
from src.pydantic_schemas.physical import Physical
from src.enums.user_enums import Statuses


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo
