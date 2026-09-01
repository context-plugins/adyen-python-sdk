from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount32 import Amount32, Amount32Dict
from .billing_address4 import BillingAddress4, BillingAddress4Dict


class SubMerchantInfo(SdkBaseModel):
    address: Optional[BillingAddress4] = UNSET
    """Required for transactions performed by registered payment facilitators. The sub-merchant's address."""

    amount: Optional[Amount32] = UNSET
    """Required for transactions performed by registered payment facilitators. The amount of the payment corresponding
    to each sub-merchant. This value will be different than the request amount if shopper is purchasing items at
    different sub-merchants' shops."""

    email: Optional[str] = UNSET
    """Required for transactions performed by registered payment facilitators. The email associated with the
    sub-merchant's account."""

    id: Optional[str] = UNSET
    """Required for transactions performed by registered payment facilitators. A unique identifier that you create for
    the sub-merchant, used by schemes to identify the sub-merchant.
    * Format: Alphanumeric
    * Maximum length: 15 characters"""

    mcc: Optional[str] = UNSET
    """Required for transactions performed by registered payment facilitators. The sub-merchant's 4-digit Merchant
    Category Code (MCC).
    * Format: Numeric
    * Fixed length: 4 digits"""

    name: Optional[str] = UNSET
    """Required for transactions performed by registered payment facilitators. The name of the sub-merchant. Based on
    scheme specifications, this value will overwrite the shopper statement that will appear in the card statement.
    Exception: for acquirers in Brazil, this value does not overwrite the shopper statement.
    * Format: Alphanumeric
    * Maximum length: 22 characters"""

    phone_number: Optional[str] = Field(default=UNSET, alias="phoneNumber")
    """Required for transactions performed by registered payment facilitators. The phone number associated with the
    sub-merchant's account."""

    registered_since: Optional[str] = Field(default=UNSET, alias="registeredSince")
    tax_id: Optional[str] = Field(default=UNSET, alias="taxId")
    """Required for transactions performed by registered payment facilitators. The tax ID of the sub-merchant.
    * Format: Numeric
    * Fixed length: 11 digits for the CPF or 14 digits for the CNPJ"""

    url: Optional[str] = UNSET
    """Required for transactions performed by registered payment facilitators. The sub-merchant's URL on the platform,
    i.e. the sub-merchant's shop."""


class SubMerchantInfoDict(TypedDict):
    address: NotRequired[BillingAddress4 | BillingAddress4Dict]
    amount: NotRequired[Amount32 | Amount32Dict]
    email: NotRequired[str]
    id: NotRequired[str]
    mcc: NotRequired[str]
    name: NotRequired[str]
    phone_number: NotRequired[str]
    registered_since: NotRequired[str]
    tax_id: NotRequired[str]
    url: NotRequired[str]
