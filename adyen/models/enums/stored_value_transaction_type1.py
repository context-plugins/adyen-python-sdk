from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StoredValueTransactionType1(str, Enum):
    """Identification of operation to proceed on the stored value account or the stored value card. Possible values:
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


StoredValueTransactionType1OrStr: TypeAlias = Annotated[
    StoredValueTransactionType1 | str, open_enum_validator(StoredValueTransactionType1)
]
