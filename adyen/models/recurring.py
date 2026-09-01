from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.contract import ContractOrStr
from .enums.token_service import TokenServiceOrStr


class Recurring(SdkBaseModel):
    """The recurring settings for the payment. Use this property when you want to enable `recurring payments
    <https://docs.adyen.com/classic-integration/recurring-payments>`__., A container for the type of a recurring
    contract to be retrieved.

    The contract value needs to match the contract value submitted in the payment transaction used to create a recurring
    contract. However, if ``ONECLICK,RECURRING`` is the original contract definition in the initial payment, then
    ``contract`` should take either ``ONECLICK`` or ``RECURRING``, depending on whether or not you want the shopper to
    enter their card's security code when they finalize their purchase., A container for the type of recurring contract
    to be retrieved.

    The recurring.contract must be set to ``PAYOUT``, A container for the type of recurring contract to be retrieved.

    The ``recurring.contract`` must be set to "PAYOUT"., The recurring settings for the payment. Use this property when
    you want to enable `recurring payments <https://docs.adyen.com/classic-integration/recurring-payments>`__., The
    recurring settings for the payment. Use this property when you want to enable `recurring payments
    <https://docs.adyen.com/online-payments/tokenization>`__."""

    contract: Optional[ContractOrStr] = UNSET
    """The type of recurring contract to be used. Possible values:
    * ``ONECLICK`` – Payment details can be used to initiate a one-click payment, where the shopper enters the `card
        security code (CVC/CVV)
        <https://docs.adyen.com/payments-fundamentals/payment-glossary#card-security-code-cvc-cvv-cid>`__.
    * ``RECURRING`` – Payment details can be used without the card security code to initiate `card-not-present
        transactions <https://docs.adyen.com/payments-fundamentals/payment-glossary#card-not-present-cnp>`__.
    * ``ONECLICK,RECURRING`` – Payment details can be used regardless of whether the shopper is on your site or not.
    * ``PAYOUT`` – Payment details can be used to `make a payout
        <https://docs.adyen.com/online-payments/online-payouts>`__.
    * ``EXTERNAL`` - Use this when you store payment details and send the raw card number or network token directly in
        your API request."""

    recurring_detail_name: Optional[str] = Field(default=UNSET, alias="recurringDetailName")
    """A descriptive name for this detail."""

    recurring_expiry: Optional[RFC3339DateTime] = Field(default=UNSET, alias="recurringExpiry")
    """Date after which no further authorisations shall be performed. Only for 3D Secure 2."""

    recurring_frequency: Optional[str] = Field(default=UNSET, alias="recurringFrequency")
    """Minimum number of days between authorisations. Only for 3D Secure 2."""

    token_service: Optional[TokenServiceOrStr] = Field(default=UNSET, alias="tokenService")
    """The name of the token service."""


class RecurringDict(TypedDict):
    contract: NotRequired[ContractOrStr]
    recurring_detail_name: NotRequired[str]
    recurring_expiry: NotRequired[RFC3339DateTime]
    recurring_frequency: NotRequired[str]
    token_service: NotRequired[TokenServiceOrStr]
