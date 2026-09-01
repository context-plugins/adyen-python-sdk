from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResponseAdditionalDataCard(SdkBaseModel):
    card_alt_id: Optional[str] = Field(default=UNSET, alias="cardAltID")
    """This is an ALT ID (alternate ID) mapped to the Card PAN.

    > Returned only in case of Ecommerce Card Payment in India"""

    card_bin: Optional[str] = Field(default=UNSET, alias="cardBin")
    """The first six digits of the card number.

    This is the `Bank Identification Number (BIN)
    <https://docs.adyen.com/get-started-with-adyen/payment-glossary#bank-identification-number-bin>`__ for card numbers
    with a six-digit BIN.

    Example: 521234"""

    card_holder_name: Optional[str] = Field(default=UNSET, alias="cardHolderName")
    """The cardholder name passed in the payment request."""

    card_issuing_bank: Optional[str] = Field(default=UNSET, alias="cardIssuingBank")
    """The bank or the financial institution granting lines of credit through card association branded payment cards.
    This information can be included when available."""

    card_issuing_country: Optional[str] = Field(default=UNSET, alias="cardIssuingCountry")
    """The country where the card was issued.

    Example: US"""

    card_issuing_currency: Optional[str] = Field(default=UNSET, alias="cardIssuingCurrency")
    """The currency in which the card is issued, if this information is available. Provided as the currency code or
    currency number from the ISO-4217 standard.

    Example: USD"""

    card_payment_method: Optional[str] = Field(default=UNSET, alias="cardPaymentMethod")
    """The card payment method used for the transaction.

    Example: amex"""

    card_product_id: Optional[str] = Field(default=UNSET, alias="cardProductId")
    """The Card Product ID represents the type of card following card scheme product definitions and can be returned for
    Adyen Acquiring service level payments.

    Example values Visa:
    * **A** - Visa Traditional
    * **B** - Visa Traditional Rewards
    * **C** - Visa Signature
    * **D** - Visa Signature Preferred
    * **F** - Visa Classic

    Example values Mastercard:
    * **MCC** - Mastercard Card
    * **MCE** - Mastercard Electronic Card
    * **MCF** - Mastercard Corporate Fleet Card
    * **MCG** - Gold Mastercard Card
    * **MCH** - Mastercard Premium Charge
    * **MCI** - Mastercard Select Debit"""

    card_summary: Optional[str] = Field(default=UNSET, alias="cardSummary")
    """The last four digits of a card number.

    > Returned only in case of a card payment."""

    issuer_bin: Optional[str] = Field(default=UNSET, alias="issuerBin")
    """The first eight digits of the card number. Only returned if the card number is 16 digits or more.

    This is the `Bank Identification Number (BIN)
    <https://docs.adyen.com/get-started-with-adyen/payment-glossary#bank-identification-number-bin>`__ for card numbers
    with an eight-digit BIN.

    Example: 52123423"""


class ResponseAdditionalDataCardDict(TypedDict):
    card_alt_id: NotRequired[str]
    card_bin: NotRequired[str]
    card_holder_name: NotRequired[str]
    card_issuing_bank: NotRequired[str]
    card_issuing_country: NotRequired[str]
    card_issuing_currency: NotRequired[str]
    card_payment_method: NotRequired[str]
    card_product_id: NotRequired[str]
    card_summary: NotRequired[str]
    issuer_bin: NotRequired[str]
