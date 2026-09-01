from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OfflineProcessing(SdkBaseModel):
    chip_floor_limit: Optional[int] = Field(default=UNSET, alias="chipFloorLimit")
    """The maximum offline transaction amount for chip cards, in the processing currency and specified in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""


class OfflineProcessingDict(TypedDict):
    chip_floor_limit: NotRequired[int]
