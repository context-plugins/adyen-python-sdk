from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StoredValueAccountType(str, Enum):
    """Possible values:
    * **GiftCard**
    * **PhoneCard**
    * **Other**"""

    GIFT_CARD = "GiftCard"
    PHONE_CARD = "PhoneCard"
    OTHER = "Other"

    __str__ = str.__str__


StoredValueAccountTypeOrStr: TypeAlias = Annotated[
    StoredValueAccountType | str, open_enum_validator(StoredValueAccountType)
]
