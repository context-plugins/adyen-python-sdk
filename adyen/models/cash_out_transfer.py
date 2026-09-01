from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .enums.type121 import Type121OrStr


class CashOutTransfer(SdkBaseModel):
    amount: Amount17
    """The amount of the cashout instruction transaction, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    id: str
    """The reference of the cashout transfer."""

    type_: Type121OrStr = Field(alias="type")
    """The type of the cashout transfer.

    Possible values:
    - **cashoutRepayment**: Corresponds to the transfer created to deduct the cashout amount after settlement.
    - **cashoutFee**: Corresponds to the transfer created to debit the cashout fee form the user's balance account."""


class CashOutTransferDict(TypedDict):
    amount: Amount17 | Amount17Dict
    id: str
    type_: Type121OrStr
