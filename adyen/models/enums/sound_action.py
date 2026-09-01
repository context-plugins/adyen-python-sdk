from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SoundAction(str, Enum):
    """Possible values:
    * **StartSound**
    * **StopSound**
    * **SetDefaultVolume**"""

    START_SOUND = "StartSound"
    STOP_SOUND = "StopSound"
    SET_DEFAULT_VOLUME = "SetDefaultVolume"

    __str__ = str.__str__


SoundActionOrStr: TypeAlias = Annotated[SoundAction | str, open_enum_validator(SoundAction)]
