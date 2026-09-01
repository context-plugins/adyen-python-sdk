from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationStatus1(str, Enum):
    """The status of the verification process for the bank account.

    Possible values:
    * **valid**: the verification was successful.
    * **pending**: the verification is in progress.
    * **invalid**: the information provided is not complete.
    * **rejected**: there are reasons to refuse working with this entity."""

    INVALID = "invalid"
    PENDING = "pending"
    REJECTED = "rejected"
    VALID = "valid"

    __str__ = str.__str__


VerificationStatus1OrStr: TypeAlias = Annotated[VerificationStatus1 | str, open_enum_validator(VerificationStatus1)]
