from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SdkUiType(str, Enum):
    MULTI_SELECT = "multiSelect"
    OTHER_HTML = "otherHtml"
    OUT_OF_BAND = "outOfBand"
    SINGLE_SELECT = "singleSelect"
    TEXT = "text"

    __str__ = str.__str__


SdkUiTypeOrStr: TypeAlias = Annotated[SdkUiType | str, open_enum_validator(SdkUiType)]
