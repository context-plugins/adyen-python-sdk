from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status31(str, Enum):
    """On a terminal that supports 3G or 4G connectivity, indicates the status of the primary SIM card in the
    terminal."""

    ACTIVATED = "activated"
    DEACTIVATED = "deactivated"
    DEPRECATED = "deprecated"
    INVENTORY = "inventory"
    READY_FOR_ACTIVATION = "readyForActivation"

    __str__ = str.__str__


Status31OrStr: TypeAlias = Annotated[Status31 | str, open_enum_validator(Status31)]
