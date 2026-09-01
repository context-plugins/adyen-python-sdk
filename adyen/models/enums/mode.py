from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Mode(str, Enum):
    """Indicates the type of front end integration. Possible values:
    * **embedded** (default): Drop-in or Components integration
    * **hosted**: Hosted Checkout integration"""

    EMBEDDED = "embedded"
    HOSTED = "hosted"

    __str__ = str.__str__


ModeOrStr: TypeAlias = Annotated[Mode | str, open_enum_validator(Mode)]
