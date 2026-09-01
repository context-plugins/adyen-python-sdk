from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Category(str, Enum):
    """The type of event notification sent when you select the notification button."""

    SALE_WAKE_UP = "SaleWakeUp"
    KEY_PRESSED = "KeyPressed"

    __str__ = str.__str__


CategoryOrStr: TypeAlias = Annotated[Category | str, open_enum_validator(Category)]
