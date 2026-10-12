from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status5 import Status5OrStr
from .payment import Payment, PaymentDict


class SessionResultResponse(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """Contains additional information about the payment. Some fields are included only if you enable them. To enable
    these fields in your Customer Area, go to **Developers** > **Additional data**."""

    id: Optional[str] = UNSET
    """A unique identifier of the session."""

    payments: Optional[list[Payment]] = UNSET
    """A list of all authorised payments done for this session."""

    reference: Optional[str] = UNSET
    """The unique reference that you provided in the original ``/sessions`` request. This identifies the payment and is
    used in all communication with you about the payment status."""

    status: Optional[Status5OrStr] = UNSET
    """The status of the session. The status included in the response doesn't get updated. Don't make the request again
    to check for payment status updates.

    Possible values:
    * **completed**: the shopper completed the payment, and the payment was authorized.
    * **paymentPending**: the shopper is in the process of making the payment. This applies to payment methods with an
        asynchronous flow, like voucher payments where the shopper completes the payment in a physical shop.
    * **refused**: the session has been refused, because of too many refused payment attempts. The shopper can no longer
        complete the payment with this session.
    * **canceled**: the shopper canceled the payment.
    * **expired**: the session expired. The shopper can no longer complete the payment with this session. By default,
        the session expires one hour after it is created."""


class SessionResultResponseDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    id: NotRequired[str]
    payments: NotRequired[list[PaymentDict]]
    reference: NotRequired[str]
    status: NotRequired[Status5OrStr]
