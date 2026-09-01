from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ResponseMode(str, Enum):
    """Possible values:
    * **NotRequired**
    * **Immediate**
    * **PrintEnd**
    * **SoundEnd**"""

    NOT_REQUIRED = "NotRequired"
    IMMEDIATE = "Immediate"
    PRINT_END = "PrintEnd"
    SOUND_END = "SoundEnd"

    __str__ = str.__str__


ResponseModeOrStr: TypeAlias = Annotated[ResponseMode | str, open_enum_validator(ResponseMode)]
