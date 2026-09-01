from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class InterchangeData(SdkBaseModel):
    interchange_amount: Optional[Amount17] = Field(default=UNSET, alias="interchangeAmount")
    """The currency and value of the adjusted interchange fee."""

    interchange_rate_indicator: Optional[str] = Field(default=UNSET, alias="interchangeRateIndicator")
    """A 3-character alphanumeric code assigned by Visa that identifies the specific interchange reimbursement program a
    transaction qualified for. The code is assigned based on the card type, entry mode, and security data provided."""

    type_: Literal["interchangeData"] = Field(default="interchangeData", alias="type")
    """The type of events data.

    Possible values:

     - **interchangeData**: information about the interchange fee applied to a transaction."""


class InterchangeDataDict(TypedDict):
    interchange_amount: NotRequired[Amount17 | Amount17Dict]
    interchange_rate_indicator: NotRequired[str]
    type_: NotRequired[Literal["interchangeData"]]
