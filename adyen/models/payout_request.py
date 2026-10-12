from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .amount import Amount, AmountDict
from .card import Card, CardDict
from .enums.shopper_interaction import ShopperInteractionOrStr
from .fund_source11 import FundSource11, FundSource11Dict
from .name import Name, NameDict
from .recurring import Recurring, RecurringDict


class PayoutRequest(SdkBaseModel):
    amount: Amount
    """The amount information for the transaction (in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__). For `BIN or card verification
    <https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification>`__ requests, set amount to 0
    (zero)."""

    billing_address: Optional[Address] = Field(default=UNSET, alias="billingAddress")
    """The address where to send the invoice.
    > The ``billingAddress`` object is required in the following scenarios. Include all of the fields within this
        object.
    >* For 3D Secure 2 transactions in all browser-based and mobile implementations. >* For cross-border payouts to and
    from Canada."""

    card: Optional[Card] = UNSET
    """A container for card data.
    > Either ``bankAccount`` or ``card`` field must be provided in a payment request."""

    fraud_offset: Optional[int] = Field(default=UNSET, alias="fraudOffset")
    """An integer value that is added to the normal fraud score. The value can be either positive or negative."""

    fund_source: Optional[FundSource11] = Field(default=UNSET, alias="fundSource")
    """The person or entity funding the money."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    recurring: Optional[Recurring] = UNSET
    """The recurring settings for the payment. Use this property when you want to enable `recurring payments
    <https://docs.adyen.com/classic-integration/recurring-payments>`__."""

    reference: str
    """The reference to uniquely identify a payment. This reference is used in all communication with you about the
    payment status. We recommend using a unique value per payment; however, it is not a requirement. If you need to
    provide multiple references for a transaction, separate them with hyphens ("-"). Maximum length: 80 characters."""

    selected_recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="selectedRecurringDetailReference")
    """The ``recurringDetailReference`` you want to use for this payment. The value ``LATEST`` can be used to select the
    most recently stored recurring detail."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The shopper's email address. We recommend that you provide this data, as it is used in velocity fraud checks. >
    Required for Visa and JCB transactions that require 3D Secure 2 authentication if you did not include the
    ``telephoneNumber``."""

    shopper_interaction: Optional[ShopperInteractionOrStr] = Field(default=UNSET, alias="shopperInteraction")
    """Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a
    returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction by default.

    This field has the following possible values:
    * ``Ecommerce`` - Online transactions where the cardholder is present (online). For better authorisation rates, we
        recommend sending the card security code (CSC) along with the request.
    * ``ContAuth`` - Card on file and/or subscription transactions, where the cardholder is known to the merchant
        (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation
        (one-click payment).
    * ``Moto`` - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email
        or telephone.
    * ``POS`` - Point-of-sale transactions where the shopper is physically present to make a payment using a secure
        payment terminal."""

    shopper_name: Optional[Name] = Field(default=UNSET, alias="shopperName")
    """The shopper's full name."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """Required for recurring payments. Your reference to uniquely identify this shopper, for example user ID or account
    ID. The value is case-sensitive and must be at least three characters.
    > Your reference must not include personally identifiable information (PII) such as name or email address."""

    telephone_number: Optional[str] = Field(default=UNSET, alias="telephoneNumber")
    """The shopper's telephone number.
     The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15
        digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``."""


class PayoutRequestDict(TypedDict):
    amount: AmountDict
    billing_address: NotRequired[AddressDict]
    card: NotRequired[CardDict]
    fraud_offset: NotRequired[int]
    fund_source: NotRequired[FundSource11Dict]
    merchant_account: str
    recurring: NotRequired[RecurringDict]
    reference: str
    selected_recurring_detail_reference: NotRequired[str]
    shopper_email: NotRequired[str]
    shopper_interaction: NotRequired[ShopperInteractionOrStr]
    shopper_name: NotRequired[NameDict]
    shopper_reference: NotRequired[str]
    telephone_number: NotRequired[str]
