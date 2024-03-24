from enum import Enum
from src.baseclasses.pyenum import PyEnum


class Genders(Enum):
    female = "female"
    male = "male"


class Statuses(PyEnum):
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"
