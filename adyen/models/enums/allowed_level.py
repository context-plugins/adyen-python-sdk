from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AllowedLevel(str, Enum):
    """The capability level that is allowed for the account holder.

    Possible values: **notApplicable**, **low**, **medium**, **high**., The capability level that is allowed for the
    legal entity.

    Possible values: **notApplicable**, **low**, **medium**, **high**., The requested level of the capability. Some
    capabilities, such as those used in `card issuing
    <https://docs.adyen.com/issuing/add-capabilities#capability-levels>`__, have different levels. Levels increase the
    capability, but also require additional checks and increased monitoring.

    Possible values: **notApplicable**, **low**, **medium**, **high**."""

    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"
    NOT_APPLICABLE = "notApplicable"

    __str__ = str.__str__


AllowedLevelOrStr: TypeAlias = Annotated[AllowedLevel | str, open_enum_validator(AllowedLevel)]
