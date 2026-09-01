from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ThreeDsversion(str, Enum):
    """The version of 3D Secure to use.

    Possible values:

    * **2.1.0**
    * **2.2.0**"""

    _2_1_0 = "2.1.0"
    _2_2_0 = "2.2.0"

    __str__ = str.__str__


ThreeDsversionOrStr: TypeAlias = Annotated[ThreeDsversion | str, open_enum_validator(ThreeDsversion)]
