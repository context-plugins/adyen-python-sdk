from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PinrequestType(str, Enum):
    """Type of PIN Service. Possible values:
    * **PINVerify**
    * **PINVerifyOnly**
    * **PINEnter**"""

    PIN_VERIFY = "PINVerify"
    PIN_VERIFY_ONLY = "PINVerifyOnly"
    PIN_ENTER = "PINEnter"

    __str__ = str.__str__


PinrequestTypeOrStr: TypeAlias = Annotated[PinrequestType | str, open_enum_validator(PinrequestType)]
