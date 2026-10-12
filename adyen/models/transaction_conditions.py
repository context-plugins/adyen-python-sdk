from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.force_entry_mode import ForceEntryModeOrStr
from .enums.loyalty_handling1 import LoyaltyHandling1OrStr


class TransactionConditions(SdkBaseModel):
    """Conditions on which the transaction must be processed."""

    allowed_payment_brand: Optional[list[str]] = Field(default=UNSET, alias="AllowedPaymentBrand")
    """Payment brands accepted for this transaction. Card payment brands allowed by the Sale System for the payment
    transaction. Restrict brand if data sent."""

    acquirer_id: Optional[list[int]] = Field(default=UNSET, alias="AcquirerID")
    """Identification of the Acquirer. Restrict to these Acquirer if present."""

    debit_preferred_flag: Optional[bool] = Field(default=UNSET, alias="DebitPreferredFlag")
    """The preferred type of payment is a debit transaction rather than a credit transaction."""

    allowed_loyalty_brand: Optional[list[str]] = Field(default=UNSET, alias="AllowedLoyaltyBrand")
    """Loyalty brands or programs allowed by the Sale System for the loyalty transaction. Restrict brand if data
    sent."""

    loyalty_handling: Optional[LoyaltyHandling1OrStr] = Field(default=UNSET, alias="LoyaltyHandling")
    """Type of Loyalty processing requested by the Sale System. Possible values:
    * **Allowed**
    * **Forbidden**
    * **Processed**
    * **Proposed**
    * **Required**"""

    customer_language: Optional[str] = Field(default=UNSET, alias="CustomerLanguage")
    """The language used on the terminal screen or in text printed by the terminal. Typical use case is setting the
    language on unattended terminals. Format: two-character `ISO 639:2023
    <https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes>`__ format."""

    force_online_flag: bool = Field(default=False, alias="ForceOnlineFlag")
    """Indicates if the Cashier requires POI forces online access to the Acquirer. Go online if data sent."""

    force_entry_mode: Optional[list[ForceEntryModeOrStr]] = Field(default=UNSET, alias="ForceEntryMode")
    """Payment instrument entry mode requested by the Sale System. Restrict entry mode if sent. Possible values:
    * **CheckReader**
    * **Contactless**
    * **File**
    * **ICC**
    * **Keyed**
    * **MagStripe**
    * **Manual**
    * **RFID**
    * **Scanned**
    * **SynchronousICC**
    * **Tapped**"""

    merchant_category_code: Optional[str] = Field(default=UNSET, alias="MerchantCategoryCode")
    """The code which identifies the category of the transaction (MCC). The payment implies a specific MCC."""


class TransactionConditionsDict(TypedDict):
    allowed_payment_brand: NotRequired[list[str]]
    acquirer_id: NotRequired[list[int]]
    debit_preferred_flag: NotRequired[bool]
    allowed_loyalty_brand: NotRequired[list[str]]
    loyalty_handling: NotRequired[LoyaltyHandling1OrStr]
    customer_language: NotRequired[str]
    force_online_flag: NotRequired[bool]
    force_entry_mode: NotRequired[list[ForceEntryModeOrStr]]
    merchant_category_code: NotRequired[str]
