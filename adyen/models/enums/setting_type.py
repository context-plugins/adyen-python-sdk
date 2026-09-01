from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SettingType(str, Enum):
    BALANCE = "balance"

    __str__ = str.__str__


SettingTypeOrStr: TypeAlias = Annotated[SettingType | str, open_enum_validator(SettingType)]
