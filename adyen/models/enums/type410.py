from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type410(str, Enum):
    """Type of phone number. Possible values: **Landline**, **Mobile**."""

    LANDLINE = "landline"
    MOBILE = "mobile"

    __str__ = str.__str__


Type410OrStr: TypeAlias = Annotated[Type410 | str, open_enum_validator(Type410)]
