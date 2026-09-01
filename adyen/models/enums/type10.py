from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type10(str, Enum):
    """**directdebit_GB**"""

    DIRECTDEBIT_GB = "directdebit_GB"

    __str__ = str.__str__


Type10OrStr: TypeAlias = Annotated[Type10 | str, open_enum_validator(Type10)]
