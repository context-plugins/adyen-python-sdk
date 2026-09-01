from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IdentificationSupport(str, Enum):
    """Support of the loyalty account identification. Allows knowing where and how you have found the loyalty account
    identification. Possible values:
    * **NoCard**
    * **LoyaltyCard**
    * **HybridCard**
    * **LinkedCard**"""

    NO_CARD = "NoCard"
    LOYALTY_CARD = "LoyaltyCard"
    HYBRID_CARD = "HybridCard"
    LINKED_CARD = "LinkedCard"

    __str__ = str.__str__


IdentificationSupportOrStr: TypeAlias = Annotated[
    IdentificationSupport | str, open_enum_validator(IdentificationSupport)
]
