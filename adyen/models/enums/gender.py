from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Gender(str, Enum):
    """The gender. >The following values are permitted: ``MALE``, ``FEMALE``, ``UNKNOWN``."""

    MALE = "MALE"
    FEMALE = "FEMALE"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


GenderOrStr: TypeAlias = Annotated[Gender | str, open_enum_validator(Gender)]
