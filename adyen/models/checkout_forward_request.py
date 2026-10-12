from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount11 import Amount11, Amount11Dict
from .checkout_forward_request_card2 import CheckoutForwardRequestCard2, CheckoutForwardRequestCard2Dict
from .checkout_forward_request_options2 import CheckoutForwardRequestOptions2, CheckoutForwardRequestOptions2Dict
from .checkout_outgoing_forward_request2 import CheckoutOutgoingForwardRequest2, CheckoutOutgoingForwardRequest2Dict


class CheckoutForwardRequest(SdkBaseModel):
    amount: Optional[Amount11] = UNSET
    """The amount of the forwarded payment."""

    base_url: str = Field(alias="baseUrl")
    """The base URL of the third party API, where Adyen will send the request to forward the payment details."""

    merchant_account: str = Field(alias="merchantAccount")
    """Your merchant account."""

    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """Merchant defined payment reference."""

    options: Optional[CheckoutForwardRequestOptions2] = UNSET
    """The customizations that can be applied when making a forward request."""

    payment_method: Optional[CheckoutForwardRequestCard2] = Field(default=UNSET, alias="paymentMethod")
    """The card details."""

    request: CheckoutOutgoingForwardRequest2
    """The `details of the request
    <https://docs.adyen.com/online-payments/tokenization/forward-payment-details#request-to-adyen-card>`__ that you want
    to forward to the third-party."""

    shopper_reference: str = Field(alias="shopperReference")
    """Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive
    and must be at least three characters.
    > Your reference must not include personally identifiable information (PII) such as name or email address."""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """The unique identifier of the token that you want to forward to the third party. This is the
    ``storedPaymentMethodId`` you received in the webhook after you created the token."""


class CheckoutForwardRequestDict(TypedDict):
    amount: NotRequired[Amount11Dict]
    base_url: str
    merchant_account: str
    merchant_reference: NotRequired[str]
    options: NotRequired[CheckoutForwardRequestOptions2Dict]
    payment_method: NotRequired[CheckoutForwardRequestCard2Dict]
    request: CheckoutOutgoingForwardRequest2Dict
    shopper_reference: str
    stored_payment_method_id: NotRequired[str]
