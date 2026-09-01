from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .payout_schedule_execution import PayoutScheduleExecution, PayoutScheduleExecutionDict


class PayoutScheduleExecutions(SdkBaseModel):
    payout_schedule_executions: list[PayoutScheduleExecution] = Field(alias="payoutScheduleExecutions")
    """Contains a list of executions of the payout schedule."""


class PayoutScheduleExecutionsDict(TypedDict):
    payout_schedule_executions: list[PayoutScheduleExecution | PayoutScheduleExecutionDict]
