from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SdkInterface(str, Enum):
    """Supported SDK interface types. Allowed values:
    * native
    * html
    * both"""

    NATIVE = "native"
    HTML = "html"
    BOTH = "both"

    __str__ = str.__str__


SdkInterfaceOrStr: TypeAlias = Annotated[SdkInterface | str, open_enum_validator(SdkInterface)]
