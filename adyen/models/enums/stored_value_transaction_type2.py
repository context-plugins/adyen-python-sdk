from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StoredValueTransactionType2(str, Enum):
    """Identification of operation to proceed on the stored value account or the stored value card. Copy. Possible
    values:
    * **Activate**
    * **Duplicate**
    * **Load**
    * **Reserve**
    * **Reverse**
    * **Unload**"""

    RESERVE = "Reserve"
    ACTIVATE = "Activate"
    LOAD = "Load"
    UNLOAD = "Unload"
    REVERSE = "Reverse"
    DUPLICATE = "Duplicate"

    __str__ = str.__str__


StoredValueTransactionType2OrStr: TypeAlias = Annotated[
    StoredValueTransactionType2 | str, open_enum_validator(StoredValueTransactionType2)
]
