from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .amount_adjustment import AmountAdjustment, AmountAdjustmentDict
from .balance_mutation import BalanceMutation, BalanceMutationDict
from .enums.reason1 import Reason1OrStr
from .enums.status24 import Status24OrStr
from .enums.type73 import Type73OrStr
from .external_reason1 import ExternalReason1, ExternalReason1Dict
from .modification2 import Modification2, Modification2Dict
from .unions.events_datum import EventsDatum, EventsDatumDict
from .unions.tracing_data import TracingData, TracingDataDict
from .unions.tracking_data import TrackingData, TrackingDataDict


class TransferEvent(SdkBaseModel):
    amount: Optional[Amount17] = UNSET
    """The original journal amount. Only applicable for `issuing <https://docs.adyen.com/issuing/>`__ integrations."""

    amount_adjustments: Optional[list[AmountAdjustment]] = Field(default=UNSET, alias="amountAdjustments")
    """The amount adjustments in this transfer. Only applicable for `issuing <https://docs.adyen.com/issuing/>`__
    integrations."""

    arn: Optional[str] = UNSET
    """Scheme unique arn identifier useful for tracing captures, chargebacks, refunds, etc."""

    booking_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="bookingDate")
    """The date when the transfer request was sent."""

    estimated_arrival_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="estimatedArrivalTime")
    """The estimated time when the beneficiary should have access to the funds."""

    events_data: Optional[list[EventsDatum]] = Field(default=UNSET, alias="eventsData")
    """A list of event data."""

    external_reason: Optional[ExternalReason1] = Field(default=UNSET, alias="externalReason")
    """The external reason for the transfer status."""

    id: Optional[str] = UNSET
    """The unique identifier of the transfer event."""

    modification: Optional[Modification2] = UNSET
    """The payment modification. Only applicable for `returned internal transfers
    <https://docs.adyen.com/platforms/internal-fund-transfers/internal-transfer-webhooks/#returned-internal-transfer>`__."""

    mutations: Optional[list[BalanceMutation]] = UNSET
    """The list of balance mutations per event."""

    original_amount: Optional[Amount17] = Field(default=UNSET, alias="originalAmount")
    """The amount in the original currency. Only applicable for `issuing <https://docs.adyen.com/issuing/>`__
    integrations."""

    reason: Optional[Reason1OrStr] = UNSET
    """The reason for the transfer status."""

    status: Optional[Status24OrStr] = UNSET
    """The status of the transfer event."""

    tracing_data: Optional[TracingData] = Field(default=UNSET, alias="tracingData")
    """Additional tracing information for the tracing event."""

    tracking_data: Optional[TrackingData] = Field(default=UNSET, alias="trackingData")
    """Additional information for the tracking event."""

    transaction_id: Optional[str] = Field(default=UNSET, alias="transactionId")
    """The id of the transaction that is related to this accounting event. Only sent for events of type **accounting**
    where the balance changes."""

    type_: Optional[Type73OrStr] = Field(default=UNSET, alias="type")
    """The type of the transfer event. Possible values: **accounting**, **tracking**."""

    update_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updateDate")
    """The date when the tracking status was updated."""

    value_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="valueDate")
    """The date when the funds are expected to be deducted from or credited to the balance account. This date can be in
    either the past or future."""


class TransferEventDict(TypedDict):
    amount: NotRequired[Amount17Dict]
    amount_adjustments: NotRequired[list[AmountAdjustmentDict]]
    arn: NotRequired[str]
    booking_date: NotRequired[RFC3339DateTime]
    estimated_arrival_time: NotRequired[RFC3339DateTime]
    events_data: NotRequired[list[EventsDatumDict]]
    external_reason: NotRequired[ExternalReason1Dict]
    id: NotRequired[str]
    modification: NotRequired[Modification2Dict]
    mutations: NotRequired[list[BalanceMutationDict]]
    original_amount: NotRequired[Amount17Dict]
    reason: NotRequired[Reason1OrStr]
    status: NotRequired[Status24OrStr]
    tracing_data: NotRequired[TracingDataDict]
    tracking_data: NotRequired[TrackingDataDict]
    transaction_id: NotRequired[str]
    type_: NotRequired[Type73OrStr]
    update_date: NotRequired[RFC3339DateTime]
    value_date: NotRequired[RFC3339DateTime]
