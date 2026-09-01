from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IdentificationSupport1(str, Enum):
    """Support of the loyalty account identification. Allows knowing where and how you have found the loyalty account
    identification. Possible values:
    * **HybridCard**
    * **LinkedCard**
    * **LoyaltyCard**
    * **NoCard**"""

    NO_CARD = "NoCard"
    LOYALTY_CARD = "LoyaltyCard"
    HYBRID_CARD = "HybridCard"
    LINKED_CARD = "LinkedCard"

    __str__ = str.__str__


IdentificationSupport1OrStr: TypeAlias = Annotated[
    IdentificationSupport1 | str, open_enum_validator(IdentificationSupport1)
]
