from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShareholderType(str, Enum):
    """Specifies how the person is associated with the account holder.

    Possible values:

    * **Owner**: Individuals who directly or indirectly own 25% or more of a company.

    * **Controller**: Individuals who are members of senior management staff responsible for managing a company or
        organization."""

    CONTROLLER = "Controller"
    OWNER = "Owner"
    SIGNATORY = "Signatory"

    __str__ = str.__str__


ShareholderTypeOrStr: TypeAlias = Annotated[ShareholderType | str, open_enum_validator(ShareholderType)]
