from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type31(str, Enum):
    """**genericissuer**"""

    ONLINE_BANKING_PL = "onlineBanking_PL"
    EPS = "eps"
    ONLINE_BANKING_SK = "onlineBanking_SK"
    ONLINE_BANKING_CZ = "onlineBanking_CZ"
    ONLINEBANKING_IN = "onlinebanking_IN"

    __str__ = str.__str__


Type31OrStr: TypeAlias = Annotated[Type31 | str, open_enum_validator(Type31)]
