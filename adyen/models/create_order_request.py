from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount21 import Amount21, Amount21Dict


class CreateOrderRequest(SdkBaseModel):
    amount: Amount21
    """The total amount of the order."""

    expires_at: Optional[str] = Field(default=UNSET, alias="expiresAt")
    """The date when the order should expire. If not provided, the default expiry duration is 1 day.

    `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__ format: YYYY-MM-DDThh:mm:ss+TZD, for example,
    **2020-12-18T10:15:30+01:00**."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the order."""

    reference: str
    """A custom reference identifying the order."""


class CreateOrderRequestDict(TypedDict):
    amount: Amount21 | Amount21Dict
    expires_at: NotRequired[str]
    merchant_account: str
    reference: str
