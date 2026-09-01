from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ResponseMode1(str, Enum):
    """Message response awaited by the initiator of the Request. Allows various types and synchronisation of requests
    for Print or Sound. Possible values:
    * **Immediate**
    * **NotRequired**
    * **PrintEnd**
    * **SoundEnd**"""

    NOT_REQUIRED = "NotRequired"
    IMMEDIATE = "Immediate"
    PRINT_END = "PrintEnd"
    SOUND_END = "SoundEnd"

    __str__ = str.__str__


ResponseMode1OrStr: TypeAlias = Annotated[ResponseMode1 | str, open_enum_validator(ResponseMode1)]
