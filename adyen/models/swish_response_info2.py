from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SwishResponseInfo2(SdkBaseModel):
    """**swish** or its variant details"""

    swish_number: Optional[str] = Field(default=UNSET, alias="swishNumber")
    """Swish number. Format: 10 digits without spaces. For example, **1231111111**."""


class SwishResponseInfo2Dict(TypedDict):
    swish_number: NotRequired[str]
