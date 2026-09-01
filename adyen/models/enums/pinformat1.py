from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Pinformat1(str, Enum):
    """Possible values:
    * **ISO0**
    * **ISO1**
    * **ISO2**
    * **ISO3**"""

    ISO0 = "ISO0"
    ISO1 = "ISO1"
    ISO2 = "ISO2"
    ISO3 = "ISO3"

    __str__ = str.__str__


Pinformat1OrStr: TypeAlias = Annotated[Pinformat1 | str, open_enum_validator(Pinformat1)]
