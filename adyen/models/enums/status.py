from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status(str, Enum):
    """Informs you if the name validation was performed. Possible values:

    **performed**, **notPerformed**, **notSupported**"""

    NOT_PERFORMED = "notPerformed"
    NOT_SUPPORTED = "notSupported"
    PERFORMED = "performed"

    __str__ = str.__str__


StatusOrStr: TypeAlias = Annotated[Status | str, open_enum_validator(Status)]
