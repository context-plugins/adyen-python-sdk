from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.force_entry_mode import ForceEntryModeOrStr
from .enums.loyalty_handling2 import LoyaltyHandling2OrStr
from .enums.payment_type1 import PaymentType1OrStr


class CardAcquisitionTransaction(SdkBaseModel):
    allowed_payment_brand: Optional[list[str]] = Field(default=UNSET, alias="AllowedPaymentBrand")
    """Card payment brands allowed by the Sale System for the payment transaction."""

    allowed_loyalty_brand: Optional[list[str]] = Field(default=UNSET, alias="AllowedLoyaltyBrand")
    """Loyalty brands or programs allowed by the Sale System for the loyalty transaction."""

    loyalty_handling: Optional[LoyaltyHandling2OrStr] = Field(default=UNSET, alias="LoyaltyHandling")
    """Type of Loyalty processing requested by the Sale System. An way to specify what the POI has to handle concerning
    the loyalty. Possible values:
    * **Allowed**
    * **Forbidden**
    * **Processed**
    * **Proposed**
    * **Required**"""

    customer_language: Optional[str] = Field(default=UNSET, alias="CustomerLanguage")
    """The language used on the terminal screen or in text printed by the terminal.
      Typical use case is setting the language on unattended terminals. Format: two-character `ISO 639:2023
        <https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes>`__ format."""

    force_entry_mode: Optional[list[ForceEntryModeOrStr]] = Field(default=UNSET, alias="ForceEntryMode")
    """Payment instrument entry mode requested by the Sale System. Avoid retry on an out of order card reading device,
    when the sale system knows that some card entry modes on the POI do not work. Possible values:
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

    force_customer_selection_flag: Optional[bool] = Field(default=UNSET, alias="ForceCustomerSelectionFlag")
    """Indicates if the Customer realises the selection of the card application."""

    total_amount: Optional[float] = Field(default=UNSET, alias="TotalAmount")
    """Amount of a transaction. In the Card Acquisition Request message, it allows the processing of a contactless
    card."""

    payment_type: Optional[PaymentType1OrStr] = Field(default=UNSET, alias="PaymentType")
    """Type of payment transaction. Elements requested by the Sale System that are related to the payment only. Possible
    values:
    * **CashAdvance**
    * **CashDeposit**
    * **Completion**
    * **FirstReservation**
    * **Instalment**
    * **IssuerInstalment**
    * **Normal**
    * **OneTimeReservation**
    * **PaidOut**
    * **Recurring**
    * **Refund**
    * **UpdateReservation**"""

    cash_back_flag: Optional[bool] = Field(default=UNSET, alias="CashBackFlag")
    """Cash back has been requested with the payment transaction. Allows choice of the Customer language when the POI
    displays messages or print text to Merchant interface."""


class CardAcquisitionTransactionDict(TypedDict):
    allowed_payment_brand: NotRequired[list[str]]
    allowed_loyalty_brand: NotRequired[list[str]]
    loyalty_handling: NotRequired[LoyaltyHandling2OrStr]
    customer_language: NotRequired[str]
    force_entry_mode: NotRequired[list[ForceEntryModeOrStr]]
    force_customer_selection_flag: NotRequired[bool]
    total_amount: NotRequired[float]
    payment_type: NotRequired[PaymentType1OrStr]
    cash_back_flag: NotRequired[bool]
