from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StoredValueTransactionType(str, Enum):
    """Possible values:
    * **Reserve**
    * **Activate**
    * **Load**
    * **Unload**
    * **Reverse**
    * **Duplicate**"""

    RESERVE = "Reserve"
    ACTIVATE = "Activate"
    LOAD = "Load"
    UNLOAD = "Unload"
    REVERSE = "Reverse"
    DUPLICATE = "Duplicate"

    __str__ = str.__str__


StoredValueTransactionTypeOrStr: TypeAlias = Annotated[
    StoredValueTransactionType | str, open_enum_validator(StoredValueTransactionType)
]
