from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NetworkType(str, Enum):
    """Network type for Terminal API notification webhooks. Possible values:
    * **public**
    * **local**

    Default Value: **public**."""

    LOCAL = "local"
    PUBLIC = "public"

    __str__ = str.__str__


NetworkTypeOrStr: TypeAlias = Annotated[NetworkType | str, open_enum_validator(NetworkType)]
