from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Channel3(str, Enum):
    """The platform where a payment transaction takes place. This field can be used for filtering out payment methods
    that are only available on specific platforms. Possible values:
    * iOS
    * Android
    * Web"""

    I_OS = "iOS"
    ANDROID = "Android"
    WEB = "Web"

    __str__ = str.__str__


Channel3OrStr: TypeAlias = Annotated[Channel3 | str, open_enum_validator(Channel3)]
