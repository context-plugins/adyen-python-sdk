from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .duplicate_info1 import DuplicateInfo1, DuplicateInfo1Dict
from .enums.dispute_status1 import DisputeStatus1OrStr
from .fraud_info1 import FraudInfo1, FraudInfo1Dict
from .not_delivered_info1 import NotDeliveredInfo1, NotDeliveredInfo1Dict
from .other_info3 import OtherInfo3, OtherInfo3Dict


class DisputeRequest(SdkBaseModel):
    description: Optional[str] = UNSET
    """Your description for the dispute."""

    disputed_amount: Optional[Amount17] = Field(default=UNSET, alias="disputedAmount")
    """The amount for which you dispute the transaction. The disputed amount cannot be greater than the transaction
    amount. If you do not provide an amount, the entire transaction amount will be disputed."""

    duplicate_info: Optional[DuplicateInfo1] = Field(default=UNSET, alias="duplicateInfo")
    """Additional information for raising a dispute of ``type`` **duplicate**. Required for disputes of ``type``
    **duplicate**."""

    fraud_info: Optional[FraudInfo1] = Field(default=UNSET, alias="fraudInfo")
    """Additional information for raising a dispute of ``type`` **fraud**. Required for disputes of ``type``
    **fraud**."""

    not_delivered_info: Optional[NotDeliveredInfo1] = Field(default=UNSET, alias="notDeliveredInfo")
    """Additional information for raising a dispute of ``type`` **notDelivered**. Required for disputes of ``type``
    **notDelivered**."""

    other_info: Optional[OtherInfo3] = Field(default=UNSET, alias="otherInfo")
    """Additional information for raising a dispute of ``type`` **other**. Required for disputes of ``type`` **other**.

    **Note:** The **other** dispute ``type`` is currently in beta testing. Do not create or submit any disputes for this
    dispute ``type`` at this time."""

    status: Optional[DisputeStatus1OrStr] = UNSET
    """The current status of the dispute.

    When you create a dispute, you can only set the ``status`` to **draft**. When you update a dispute, you can set the
    ``status`` to **submitted** or **closed**.

    Possible values: **draft**, **submitted**, **closed**, **won**, **chargeback**, **secondPresentment**."""

    transaction_id: str = Field(alias="transactionId")
    """The unique reference of the transaction for which you are raising the dispute."""

    type_: str = Field(alias="type")
    """The type of the dispute.

    Possible values: **duplicate**, **fraud**, **notDelivered**, **other**.

    **Note:** The **other** dispute ``type`` is currently in beta testing. Do not create or submit any disputes for this
    dispute ``type`` at this time."""


class DisputeRequestDict(TypedDict):
    description: NotRequired[str]
    disputed_amount: NotRequired[Amount17Dict]
    duplicate_info: NotRequired[DuplicateInfo1Dict]
    fraud_info: NotRequired[FraudInfo1Dict]
    not_delivered_info: NotRequired[NotDeliveredInfo1Dict]
    other_info: NotRequired[OtherInfo3Dict]
    status: NotRequired[DisputeStatus1OrStr]
    transaction_id: str
    type_: str
