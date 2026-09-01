from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CardholderReceipt(SdkBaseModel):
    header_for_authorized_receipt: Optional[str] = Field(default=UNSET, alias="headerForAuthorizedReceipt")
    """The structure of the header to show on the shopper receipt. You can define the order of one or two header lines
    and blank lines. For example, **header1,header2,filler**. The text of the header lines is defined in the Customer
    Area under **In-person payments** > **Terminal settings** > **Receipts** in the **Receipt lines** block."""


class CardholderReceiptDict(TypedDict):
    header_for_authorized_receipt: NotRequired[str]
