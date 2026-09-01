from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Channel2(str, Enum):
    """The platform where a payment transaction takes place. This field is optional for filtering out payment methods
    that are only available on specific platforms. If this value is not set, then we will try to infer it from the
    ``sdkVersion`` or ``token``.

    Possible values:
    * iOS
    * Android
    * Web"""

    I_OS = "iOS"
    ANDROID = "Android"
    WEB = "Web"

    __str__ = str.__str__


Channel2OrStr: TypeAlias = Annotated[Channel2 | str, open_enum_validator(Channel2)]
