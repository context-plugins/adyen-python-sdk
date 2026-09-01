from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncludeMode(str, Enum):
    """Indicates whether the specified ``eventType`` is sent to your webhook endpoint. Possible values:
    * **INCLUDE**: Send the specified ``eventType``.
    * **EXCLUDE**: Send all event types except the specified ``eventType`` and other event types with the
        ``includeMode`` set to **EXCLUDE**."""

    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"

    __str__ = str.__str__


IncludeModeOrStr: TypeAlias = Annotated[IncludeMode | str, open_enum_validator(IncludeMode)]
