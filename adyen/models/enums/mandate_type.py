from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MandateType(str, Enum):
    BACS = "bacs"

    __str__ = str.__str__


MandateTypeOrStr: TypeAlias = Annotated[MandateType | str, open_enum_validator(MandateType)]
