from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IssuingTransactionData(SdkBaseModel):
    capture_cycle_id: Optional[str] = Field(default=UNSET, alias="captureCycleId")
    """captureCycleId associated with transfer event."""

    type_: Literal["issuingTransactionData"] = Field(default="issuingTransactionData", alias="type")
    """The type of events data.

    Possible values:

     - **issuingTransactionData**: issuing transaction data"""


class IssuingTransactionDataDict(TypedDict):
    capture_cycle_id: NotRequired[str]
    type_: Literal["issuingTransactionData"]
