from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Code(str, Enum):
    """The code for the status of the grant. Possible values:
    - **Pending**
    - **Active**
    - **Repaid**
    - **WrittenOff**
    - **Failed**
    - **Revoked**
    - **Requested**
    - **Reviewing**
    - **Approved**
    - **Rejected**
    - **Cancelled**"""

    PENDING = "Pending"
    ACTIVE = "Active"
    REPAID = "Repaid"
    WRITTEN_OFF = "WrittenOff"
    FAILED = "Failed"
    REVOKED = "Revoked"
    REQUESTED = "Requested"
    REVIEWING = "Reviewing"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    CANCELLED = "Cancelled"

    __str__ = str.__str__


CodeOrStr: TypeAlias = Annotated[Code | str, open_enum_validator(Code)]
