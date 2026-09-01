from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubMerchantData(SdkBaseModel):
    email: str
    """The email associated with the sub-merchant's account."""

    id: str
    """A unique identifier that you create for the sub-merchant, used by schemes to identify the sub-merchant.
    * Format: Alphanumeric
    * Maximum length: 15 characters"""

    mcc: str
    """The sub-merchant's 4-digit Merchant Category Code (MCC).
    * Format: Numeric
    * Fixed length: 4 digits"""

    name: str
    """The name of the sub-merchant. Based on scheme specifications, this value will overwrite the shopper statement
    that will appear in the card statement.
    * Format: Alphanumeric
    * Maximum length: 22 characters"""


class SubMerchantDataDict(TypedDict):
    email: str
    id: str
    mcc: str
    name: str
