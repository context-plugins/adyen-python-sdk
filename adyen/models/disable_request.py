from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DisableRequest(SdkBaseModel):
    contract: Optional[str] = UNSET
    """Specify the contract if you only want to disable a specific use.

    This field can be set to one of the following values, or to their combination (comma-separated):
    * ONECLICK
    * RECURRING
    * PAYOUT"""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier with which you want to process the transaction."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """The ID that uniquely identifies the recurring detail reference.

    If it is not provided, the whole recurring contract of the ``shopperReference`` will be disabled, which includes all
    recurring details."""

    shopper_reference: str = Field(alias="shopperReference")
    """The ID that uniquely identifies the shopper.

    This ``shopperReference`` must be the same as the ``shopperReference`` used in the initial payment."""


class DisableRequestDict(TypedDict):
    contract: NotRequired[str]
    merchant_account: str
    recurring_detail_reference: NotRequired[str]
    shopper_reference: str
