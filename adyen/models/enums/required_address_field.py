from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RequiredAddressField(str, Enum):
    CITY = "city"
    COUNTRY = "country"
    LINE1 = "line1"
    POSTAL_CODE = "postalCode"
    STATE_OR_PROVINCE = "stateOrProvince"

    __str__ = str.__str__


RequiredAddressFieldOrStr: TypeAlias = Annotated[RequiredAddressField | str, open_enum_validator(RequiredAddressField)]
