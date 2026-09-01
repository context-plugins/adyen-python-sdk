from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ResultCode3(str, Enum):
    """The result of the payment. Possible values:

    * **Success** – The operation has been completed successfully.
    * **Refused** – The operation was refused. The reason is given in the ``refusalReason`` field.
    * **Error** – There was an error when the operation was processed. The reason is given in the ``refusalReason``
        field.
    * **NotEnoughBalance** – The amount on the payment method is lower than the amount given in the request. Only
        applicable to balance checks."""

    SUCCESS = "Success"
    REFUSED = "Refused"
    ERROR = "Error"
    NOT_ENOUGH_BALANCE = "NotEnoughBalance"

    __str__ = str.__str__


ResultCode3OrStr: TypeAlias = Annotated[ResultCode3 | str, open_enum_validator(ResultCode3)]
