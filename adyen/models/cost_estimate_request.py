from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict
from .cost_estimate_assumptions1 import CostEstimateAssumptions1, CostEstimateAssumptions1Dict
from .enums.shopper_interaction import ShopperInteractionOrStr
from .merchant_details2 import MerchantDetails2, MerchantDetails2Dict
from .recurring import Recurring, RecurringDict


class CostEstimateRequest(SdkBaseModel):
    amount: Amount
    """The transaction amount used as a base for the cost estimation."""

    assumptions: Optional[CostEstimateAssumptions1] = UNSET
    """Assumptions made for the expected characteristics of the transaction, for which the charges are being
    estimated."""

    card_number: Optional[str] = Field(default=UNSET, alias="cardNumber")
    """The card number (4-19 characters) for PCI compliant use cases. Do not use any separators.

    > Either the ``cardNumber`` or ``encryptedCardNumber`` field must be provided in a payment request."""

    encrypted_card_number: Optional[str] = Field(default=UNSET, alias="encryptedCardNumber")
    """Encrypted data that stores card information for non PCI-compliant use cases. The encrypted data must be created
    with the Checkout Card Component or Secured Fields Component, and must contain the ``encryptedCardNumber`` field.

    > Either the ``cardNumber`` or ``encryptedCardNumber`` field must be provided in a payment request."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier you want to process the (transaction) request with."""

    merchant_details: Optional[MerchantDetails2] = Field(default=UNSET, alias="merchantDetails")
    """Additional data for merchants who don't use Adyen as the payment authorisation gateway."""

    recurring: Optional[Recurring] = UNSET
    """The recurring settings for the payment. Use this property when you want to enable `recurring payments
    <https://docs.adyen.com/online-payments/tokenization>`__."""

    selected_recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="selectedRecurringDetailReference")
    """The ``recurringDetailReference`` you want to use for this cost estimate. The value ``LATEST`` can be used to
    select the most recently stored recurring detail."""

    shopper_interaction: Optional[ShopperInteractionOrStr] = Field(default=UNSET, alias="shopperInteraction")
    """Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a
    returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction by default.

    This field has the following possible values:
    * ``Ecommerce`` - Online transactions where the cardholder is present (online). For better authorisation rates, we
        recommend sending the card security code (CSC) along with the request.
    * ``ContAuth`` - Card on file and/or subscription transactions, where the card holder is known to the merchant
        (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation
        (one-click payment).
    * ``Moto`` - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email
        or telephone.
    * ``POS`` - Point-of-sale transactions where the shopper is physically present to make a payment using a secure
        payment terminal."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """Required for recurring payments. Your reference to uniquely identify this shopper, for example user ID or account
    ID. The value is case-sensitive and must be at least three characters.
    > Your reference must not include personally identifiable information (PII) such as name or email address."""


class CostEstimateRequestDict(TypedDict):
    amount: AmountDict
    assumptions: NotRequired[CostEstimateAssumptions1Dict]
    card_number: NotRequired[str]
    encrypted_card_number: NotRequired[str]
    merchant_account: str
    merchant_details: NotRequired[MerchantDetails2Dict]
    recurring: NotRequired[RecurringDict]
    selected_recurring_detail_reference: NotRequired[str]
    shopper_interaction: NotRequired[ShopperInteractionOrStr]
    shopper_reference: NotRequired[str]
