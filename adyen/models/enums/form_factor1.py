from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FormFactor1(str, Enum):
    """The form factor of the card. Possible values: **virtual**, **physical**."""

    PHYSICAL = "physical"
    UNKNOWN = "unknown"
    VIRTUAL = "virtual"

    __str__ = str.__str__


FormFactor1OrStr: TypeAlias = Annotated[FormFactor1 | str, open_enum_validator(FormFactor1)]
