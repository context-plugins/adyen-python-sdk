from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type29(str, Enum):
    """**econtextvoucher**"""

    ECONTEXT_SEVEN_ELEVEN = "econtext_seven_eleven"
    ECONTEXT_ONLINE = "econtext_online"
    ECONTEXT = "econtext"
    ECONTEXT_STORES = "econtext_stores"
    ECONTEXT_ATM = "econtext_atm"

    __str__ = str.__str__


Type29OrStr: TypeAlias = Annotated[Type29 | str, open_enum_validator(Type29)]
