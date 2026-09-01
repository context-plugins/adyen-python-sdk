from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_info2 import CardInfo2, CardInfo2Dict
from .enums.status10 import Status10OrStr
from .enums.status_reason2 import StatusReason2OrStr


class PaymentInstrumentUpdateRequest(SdkBaseModel):
    balance_account_id: Optional[str] = Field(default=UNSET, alias="balanceAccountId")
    """The unique identifier of the balance account associated with this payment instrument. >You can only change the
    balance account ID if the payment instrument has **inactive** status."""

    card: Optional[CardInfo2] = UNSET
    """Object that contains information about the card payment instrument."""

    status: Optional[Status10OrStr] = UNSET
    """The status of the payment instrument. If a status is not specified when creating a payment instrument, it is set
    to **active** by default. However, there can be exceptions for cards based on the ``card.formFactor`` and the
    ``issuingCountryCode``. For example, when issuing physical cards in the US, the default status is **inactive**.

    Possible values:

     * **active**: The payment instrument is active and can be used to make payments.

     * **inactive**: The payment instrument is inactive and cannot be used to make payments.

     * **suspended**: The payment instrument is suspended, either because it was stolen or lost.

     * **closed**: The payment instrument is permanently closed. This action cannot be undone."""

    status_comment: Optional[str] = Field(default=UNSET, alias="statusComment")
    """Comment for the status of the payment instrument.

    Required if ``statusReason`` is **other**."""

    status_reason: Optional[StatusReason2OrStr] = Field(default=UNSET, alias="statusReason")
    """The reason for updating the status of the payment instrument.

    Possible values: **lost**, **stolen**, **damaged**, **suspectedFraud**, **expired**, **endOfLife**,
    **accountClosure**, **other**. If the reason is **other**, you must also send the ``statusComment`` parameter
    describing the status change."""


class PaymentInstrumentUpdateRequestDict(TypedDict):
    balance_account_id: NotRequired[str]
    card: NotRequired[CardInfo2 | CardInfo2Dict]
    status: NotRequired[Status10OrStr]
    status_comment: NotRequired[str]
    status_reason: NotRequired[StatusReason2OrStr]
