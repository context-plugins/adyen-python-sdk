from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .airline11 import Airline11, Airline11Dict
from .lodging1 import Lodging1, Lodging1Dict


class MerchantPurchaseData(SdkBaseModel):
    airline: Optional[Airline11] = UNSET
    """Airline information."""

    lodging: Optional[list[Lodging1]] = UNSET
    """Lodging information."""

    type_: Literal["merchantPurchaseData"] = Field(default="merchantPurchaseData", alias="type")
    """The type of events data.

    Possible values:

     - **merchantPurchaseData**: merchant purchase data"""


class MerchantPurchaseDataDict(TypedDict):
    airline: NotRequired[Airline11Dict]
    lodging: NotRequired[list[Lodging1Dict]]
    type_: Literal["merchantPurchaseData"]
