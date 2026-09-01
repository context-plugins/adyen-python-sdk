from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SwishInfo(SdkBaseModel):
    swish_number: str = Field(alias="swishNumber")
    """Swish number. Format: 10 digits without spaces. For example, **1231111111**."""


class SwishInfoDict(TypedDict):
    swish_number: str
