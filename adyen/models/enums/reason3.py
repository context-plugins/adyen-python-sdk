from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Reason3(str, Enum):
    """The reason why the web data was not provided. Possible value: **noOnlinePresence**."""

    NO_ONLINE_PRESENCE = "noOnlinePresence"
    NOT_COLLECTED_DURING_ONBOARDING = "notCollectedDuringOnboarding"

    __str__ = str.__str__


Reason3OrStr: TypeAlias = Annotated[Reason3 | str, open_enum_validator(Reason3)]
