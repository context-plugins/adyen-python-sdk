from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SoundFormat(str, Enum):
    """Possible values:
    * **SoundRef**
    * **MessageRef**
    * **Text**"""

    SOUND_REF = "SoundRef"
    MESSAGE_REF = "MessageRef"
    TEXT = "Text"

    __str__ = str.__str__


SoundFormatOrStr: TypeAlias = Annotated[SoundFormat | str, open_enum_validator(SoundFormat)]
