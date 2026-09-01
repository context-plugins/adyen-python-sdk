from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .recurring_detail_wrapper import RecurringDetailWrapper, RecurringDetailWrapperDict


class RecurringDetailsResult(SdkBaseModel):
    creation_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="creationDate")
    """The date when the recurring details were created."""

    details: Optional[list[RecurringDetailWrapper]] = UNSET
    """Payment details stored for recurring payments."""

    last_known_shopper_email: Optional[str] = Field(default=UNSET, alias="lastKnownShopperEmail")
    """The most recent email for this shopper (if available)."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """The reference you use to uniquely identify the shopper (e.g. user ID or account ID)."""


class RecurringDetailsResultDict(TypedDict):
    creation_date: NotRequired[RFC3339DateTime]
    details: NotRequired[list[RecurringDetailWrapper | RecurringDetailWrapperDict]]
    last_known_shopper_email: NotRequired[str]
    shopper_reference: NotRequired[str]
