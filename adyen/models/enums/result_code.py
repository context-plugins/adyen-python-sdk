from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ResultCode(str, Enum):
    """The result of the cancellation request.

    Possible values:

    * **Success** – Indicates that the balance check was successful.
    * **NotEnoughBalance** – Commonly indicates that the card did not have enough balance to pay the amount in the
        request, or that the currency of the balance on the card did not match the currency of the requested amount.
    * **Failed** – Indicates that the balance check failed."""

    SUCCESS = "Success"
    NOT_ENOUGH_BALANCE = "NotEnoughBalance"
    FAILED = "Failed"

    __str__ = str.__str__


ResultCodeOrStr: TypeAlias = Annotated[ResultCode | str, open_enum_validator(ResultCode)]
