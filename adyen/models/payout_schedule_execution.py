from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.execution_result1 import ExecutionResult1OrStr
from .payout_schedule_execution_details2 import PayoutScheduleExecutionDetails2, PayoutScheduleExecutionDetails2Dict


class PayoutScheduleExecution(SdkBaseModel):
    id: Optional[str] = UNSET
    """The unique identifier of the payout execution."""

    result: Optional[ExecutionResult1OrStr] = UNSET
    """The status of the payout execution.

    Possible values:
    - **succeeded**: The payout was sent successfully.
    - **failed**: The payout could not be sent because an error occurred.
    - **skipped**: The payout was not triggered as expected."""

    result_details: Optional[PayoutScheduleExecutionDetails2] = Field(default=UNSET, alias="resultDetails")
    """Contains information about the result of the payout execution."""

    triggered_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="triggeredAt")
    """The date and time when the payout execution was initiated."""


class PayoutScheduleExecutionDict(TypedDict):
    id: NotRequired[str]
    result: NotRequired[ExecutionResult1OrStr]
    result_details: NotRequired[PayoutScheduleExecutionDetails2Dict]
    triggered_at: NotRequired[RFC3339DateTime]
