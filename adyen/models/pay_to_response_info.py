from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayToResponseInfo(SdkBaseModel):
    merchant_name: Optional[str] = Field(default=UNSET, alias="merchantName")
    """Merchant name displayed to the shopper in the Agreements"""

    pay_to_purpose: Optional[str] = Field(default=UNSET, alias="payToPurpose")
    """Represents the purpose of the Agreements created, it relates to the business type **Allowed values**: mortgage,
    utility, loan, gambling, retail, salary, personal, government, pension, tax, other"""


class PayToResponseInfoDict(TypedDict):
    merchant_name: NotRequired[str]
    pay_to_purpose: NotRequired[str]
