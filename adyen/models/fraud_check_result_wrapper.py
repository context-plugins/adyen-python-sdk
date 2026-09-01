from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fraud_check_result import FraudCheckResult, FraudCheckResultDict


class FraudCheckResultWrapper(SdkBaseModel):
    fraud_check_result: Optional[FraudCheckResult] = Field(default=UNSET, alias="FraudCheckResult")


class FraudCheckResultWrapperDict(TypedDict):
    fraud_check_result: NotRequired[FraudCheckResult | FraudCheckResultDict]
