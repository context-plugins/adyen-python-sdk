from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MandateType2(str, Enum):
    """The type of mandate. Possible value: **bacs**."""

    BACS = "bacs"

    __str__ = str.__str__


MandateType2OrStr: TypeAlias = Annotated[MandateType2 | str, open_enum_validator(MandateType2)]
