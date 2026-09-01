from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferType(str, Enum):
    """The type of transfer to which the limit applies. Possible values:
    * **instant**: the limit applies to transfers with an **instant** priority.
    * **all**: the limit applies to all transfers, regardless of priority."""

    INSTANT = "instant"
    ALL = "all"

    __str__ = str.__str__


TransferTypeOrStr: TypeAlias = Annotated[TransferType | str, open_enum_validator(TransferType)]
