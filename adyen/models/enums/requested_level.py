from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RequestedLevel(str, Enum):
    """The requested level of the capability. Some capabilities, such as those used in `card issuing
    <https://docs.adyen.com/issuing/add-capabilities#capability-levels>`__, have different levels. Levels increase the
    capability, but also require additional checks and increased monitoring.

    Possible values: **notApplicable**, **low**, **medium**, **high**."""

    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"
    NOT_APPLICABLE = "notApplicable"

    __str__ = str.__str__


RequestedLevelOrStr: TypeAlias = Annotated[RequestedLevel | str, open_enum_validator(RequestedLevel)]
