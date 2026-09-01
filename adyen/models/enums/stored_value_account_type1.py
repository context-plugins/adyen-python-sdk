from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StoredValueAccountType1(str, Enum):
    """Type of stored value account. Allows the distinction of the stored value instrument to access the stored value
    account. Possible values:
    * **GiftCard**
    * **Other**
    * **PhoneCard**"""

    GIFT_CARD = "GiftCard"
    PHONE_CARD = "PhoneCard"
    OTHER = "Other"

    __str__ = str.__str__


StoredValueAccountType1OrStr: TypeAlias = Annotated[
    StoredValueAccountType1 | str, open_enum_validator(StoredValueAccountType1)
]
