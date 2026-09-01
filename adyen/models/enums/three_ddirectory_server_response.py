from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ThreeDdirectoryServerResponse(str, Enum):
    """3D Secure server response. It notifies whether the specified card holder is enrolled in a 3D Secure service.
    Possible values:

    * Y (Authentication available)
    * N (Card holder not enrolled/not participating)
    * U (Unable to authenticate)"""

    N = "N"
    U = "U"
    Y = "Y"

    __str__ = str.__str__


ThreeDdirectoryServerResponseOrStr: TypeAlias = Annotated[
    ThreeDdirectoryServerResponse | str, open_enum_validator(ThreeDdirectoryServerResponse)
]
