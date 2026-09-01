from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SoundFormat1(str, Enum):
    """Possible values:
    * **MessageRef**
    * **SoundRef**
    * **Text**"""

    SOUND_REF = "SoundRef"
    MESSAGE_REF = "MessageRef"
    TEXT = "Text"

    __str__ = str.__str__


SoundFormat1OrStr: TypeAlias = Annotated[SoundFormat1 | str, open_enum_validator(SoundFormat1)]
