from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class TransactionIdtype3(SdkBaseModel):
    """Reference to the last CardAcquisition, to use the same card. If the loyalty account ID comes from a previous
    CardAcquisition."""

    transaction_id: str = Field(alias="TransactionID")
    """Unique identification of a transaction to identify the transaction on the Sale System (e.g. ticket number), or
    the POI System."""

    time_stamp: RFC3339DateTime = Field(alias="TimeStamp")
    """Date and time of a transaction for the Sale System, the POI System or the Acquirer.
     Ensures the uniqueness of a transaction and indicates the time when the event
     occurs in the EventNotification message."""


class TransactionIdtype3Dict(TypedDict):
    transaction_id: str
    time_stamp: RFC3339DateTime
