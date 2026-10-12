from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..apple_pay_donations import ApplePayDonations, ApplePayDonationsDict
from ..card_donations import CardDonations, CardDonationsDict
from ..google_pay_donations import GooglePayDonations, GooglePayDonationsDict
from ..ideal_donations import IdealDonations, IdealDonationsDict
from ..pay_with_google_donations import PayWithGoogleDonations, PayWithGoogleDonationsDict
from ..stored_payment_method1 import StoredPaymentMethod1, StoredPaymentMethod1Dict

PaymentMethod1: TypeAlias = Annotated[
    (
        Annotated[ApplePayDonations, Tag("applepay")]
        | Annotated[CardDonations, Tag("scheme")]
        | Annotated[CardDonations, Tag("networkToken")]
        | Annotated[CardDonations, Tag("card")]
        | Annotated[GooglePayDonations, Tag("googlepay")]
        | Annotated[IdealDonations, Tag("ideal")]
        | Annotated[PayWithGoogleDonations, Tag("paywithgoogle")]
        | Annotated[StoredPaymentMethod1, Tag("sepadirectdebit")]
    ),
    WireDiscriminator("type"),
]
"""The type and required details of a payment method to use.

When ``donationToken`` is provided, the payment method is derived from the token and this field becomes optional.

If you are `PCI compliant <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__, and make donations
using raw card details, you must explicitly provide the payment method details."""

PaymentMethod1Dict: TypeAlias = (
    ApplePayDonationsDict
    | CardDonationsDict
    | GooglePayDonationsDict
    | IdealDonationsDict
    | PayWithGoogleDonationsDict
    | StoredPaymentMethod1Dict
)
