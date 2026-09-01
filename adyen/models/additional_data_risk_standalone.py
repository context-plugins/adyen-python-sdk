from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataRiskStandalone(SdkBaseModel):
    pay_pal_country_code: Optional[str] = Field(default=UNSET, alias="PayPal.CountryCode")
    """Shopper's country of residence in the form of ISO standard 3166 2-character country codes."""

    pay_pal_email_id: Optional[str] = Field(default=UNSET, alias="PayPal.EmailId")
    """Shopper's email."""

    pay_pal_first_name: Optional[str] = Field(default=UNSET, alias="PayPal.FirstName")
    """Shopper's first name."""

    pay_pal_last_name: Optional[str] = Field(default=UNSET, alias="PayPal.LastName")
    """Shopper's last name."""

    pay_pal_payer_id: Optional[str] = Field(default=UNSET, alias="PayPal.PayerId")
    """Unique PayPal Customer Account identification number. Character length and limitations: 13 single-byte
    alphanumeric characters."""

    pay_pal_phone: Optional[str] = Field(default=UNSET, alias="PayPal.Phone")
    """Shopper's phone number."""

    pay_pal_protection_eligibility: Optional[str] = Field(default=UNSET, alias="PayPal.ProtectionEligibility")
    """Allowed values:
    * **Eligible** — Merchant is protected by PayPal's Seller Protection Policy for Unauthorized Payments and Item Not
        Received.

    * **PartiallyEligible** — Merchant is protected by PayPal's Seller Protection Policy for Item Not Received.

    * **Ineligible** — Merchant is not protected under the Seller Protection Policy."""

    pay_pal_transaction_id: Optional[str] = Field(default=UNSET, alias="PayPal.TransactionId")
    """Unique transaction ID of the payment."""

    avs_result_raw: Optional[str] = Field(default=UNSET, alias="avsResultRaw")
    """Raw AVS result received from the acquirer, where available. Example: D"""

    bin: Optional[str] = UNSET
    """The Bank Identification Number of a credit card, which is the first six digits of a card number. Required for
    `tokenized card request <https://docs.adyen.com/online-payments/tokenization>`__."""

    cvc_result_raw: Optional[str] = Field(default=UNSET, alias="cvcResultRaw")
    """Raw CVC result received from the acquirer, where available. Example: 1"""

    risk_token: Optional[str] = Field(default=UNSET, alias="riskToken")
    """Unique identifier or token for the shopper's card details."""

    three_d_authenticated: Optional[str] = Field(default=UNSET, alias="threeDAuthenticated")
    """A Boolean value indicating whether 3DS authentication was completed on this payment. Example: true"""

    three_d_offered: Optional[str] = Field(default=UNSET, alias="threeDOffered")
    """A Boolean value indicating whether 3DS was offered for this payment. Example: true"""

    token_data_type: Optional[str] = Field(default=UNSET, alias="tokenDataType")
    """Required for PayPal payments only. The only supported value is: **paypal**."""


class AdditionalDataRiskStandaloneDict(TypedDict):
    pay_pal_country_code: NotRequired[str]
    pay_pal_email_id: NotRequired[str]
    pay_pal_first_name: NotRequired[str]
    pay_pal_last_name: NotRequired[str]
    pay_pal_payer_id: NotRequired[str]
    pay_pal_phone: NotRequired[str]
    pay_pal_protection_eligibility: NotRequired[str]
    pay_pal_transaction_id: NotRequired[str]
    avs_result_raw: NotRequired[str]
    bin: NotRequired[str]
    cvc_result_raw: NotRequired[str]
    risk_token: NotRequired[str]
    three_d_authenticated: NotRequired[str]
    three_d_offered: NotRequired[str]
    token_data_type: NotRequired[str]
