from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScaStatus(str, Enum):
    """The status of Strong Customer Authentication (SCA). Possible values:
    * **notPerformed**: the requester was unable to successfully authenticate the request using SCA, or has an SCA
        exemption.
    * **pending**: the request is pending SCA authentication.
    * **performed**: the request is successfully authenticated using SCA."""

    NOT_PERFORMED = "notPerformed"
    PENDING = "pending"
    PERFORMED = "performed"

    __str__ = str.__str__


ScaStatusOrStr: TypeAlias = Annotated[ScaStatus | str, open_enum_validator(ScaStatus)]
