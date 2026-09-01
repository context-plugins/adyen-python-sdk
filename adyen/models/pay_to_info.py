from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PayToInfo(SdkBaseModel):
    merchant_name: str = Field(alias="merchantName")
    """Merchant name displayed to the shopper in the Agreements"""

    pay_to_purpose: str = Field(alias="payToPurpose")
    """Represents the purpose of the Agreements created, it relates to the business type **Allowed values**: mortgage,
    utility, loan, gambling, retail, salary, personal, government, pension, tax, other"""


class PayToInfoDict(TypedDict):
    merchant_name: str
    pay_to_purpose: str
