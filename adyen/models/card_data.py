from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.entry_mode import EntryModeOrStr
from .payment_token1 import PaymentToken1, PaymentToken1Dict
from .sensitive_card_data1 import SensitiveCardData1, SensitiveCardData1Dict


class CardData(SdkBaseModel):
    """Information related to the payment card used for the transaction. Allows acquisition of the card data by the Sale
    System before the Payment, CardAcquisition, or BalanceInquiry request to the POI. It can also be sent in the
    CardAcquisition response, to be processed by the Sale System."""

    payment_brand: Optional[str] = Field(default=UNSET, alias="PaymentBrand")
    """Type of payment card. If card PAN is readable. Indicates the card used to pay in the PaymentResponse. Sent in the
    CardAcquisitionResponse, to leave the Cashier to choose between several applications in a smartcard, or several
    brand in a co-branded card. In this case, the CardAcquisitionRequest.ForceCustomerSelectionFlag must contain the
    value False. Brands are part of the POI and Sale Systems configurations."""

    masked_pan: Optional[str] = Field(default=UNSET, alias="MaskedPan")
    """Masked Primary Account Number Part of the PAN is replaced by a string of * characters, to identify a customer
    account or relationship. Presence of this data element, which replace the PAN when SensitiveCardData is protected
    and replaced by ProtectedCardData. Alternatively the MaskedPAN can be used as a token to identify a customer."""

    payment_account_ref: Optional[str] = Field(default=UNSET, alias="PaymentAccountRef")
    """Reference of the PAN, which identifies the PAN or the card uniquely, named also PAR (Payment Account Reference).
    This reference may be defined by the card issuer or by a token service provider under the control of the card
    issuer, and cannot be used for a payment transaction."""

    entry_mode: Optional[list[EntryModeOrStr]] = Field(default=UNSET, alias="EntryMode")
    """Entry mode of the payment instrument information. In the Payment, Loyalty or StoredValue Request messages, it
    informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. In the
    Payment, Loyalty or StoredValue Response messages, it informs the Sale System the entry mode of the payment
    instrument. Possible values:
    * **Contactless**
    * **File**
    * **ICC**
    * **Keyed**
    * **MagStripe**
    * **Manual**
    * **Mobile**
    * **RFID**
    * **Scanned**
    * **SynchronousICC**
    * **Tapped**"""

    card_country_code: Optional[int] = Field(default=UNSET, alias="CardCountryCode")
    """Country Code attached to the card (3 numerics). If available in the card."""

    protected_card_data: Optional[str] = Field(default=UNSET, alias="ProtectedCardData")
    """Sensitive information related to the payment card, protected by CMS. SensitiveCardData protected by CMS
    EnvelopedData."""

    sensitive_card_data: Optional[SensitiveCardData1] = Field(default=UNSET, alias="SensitiveCardData")
    """Sensitive information related to the payment card, entered or read by the Sale System. If structure non empty and
    unprotected."""

    payment_token: Optional[PaymentToken1] = Field(default=UNSET, alias="PaymentToken")
    """Surrogate of the PAN (Primary Account Number) of the payment card to identify the payment mean of the customer.
    It allows, for a merchant, to identify the customer. Restriction of product payable by a card."""


class CardDataDict(TypedDict):
    payment_brand: NotRequired[str]
    masked_pan: NotRequired[str]
    payment_account_ref: NotRequired[str]
    entry_mode: NotRequired[list[EntryModeOrStr]]
    card_country_code: NotRequired[int]
    protected_card_data: NotRequired[str]
    sensitive_card_data: NotRequired[SensitiveCardData1Dict]
    payment_token: NotRequired[PaymentToken1Dict]
