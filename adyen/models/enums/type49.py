from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type49(str, Enum):
    """**riverty**"""

    RIVERTY = "riverty"
    RIVERTY_ACCOUNT = "riverty_account"
    RIVERTY_INSTALLMENTS = "riverty_installments"
    SEPADIRECTDEBIT_RIVERTY = "sepadirectdebit_riverty"

    __str__ = str.__str__


Type49OrStr: TypeAlias = Annotated[Type49 | str, open_enum_validator(Type49)]
