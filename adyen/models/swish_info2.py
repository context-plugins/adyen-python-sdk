from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SwishInfo2(SdkBaseModel):
    """Details to provide if ``type`` is **swish**.
     - This field is required only if you have a contract with Swish. Swish handles settlement directly with you (not
            through Adyen).
     - If not specified then it's assumed that you are using Adyen's contract with Swish.You don't have a direct
            relationship with Swish."""

    swish_number: str = Field(alias="swishNumber")
    """Swish number. Format: 10 digits without spaces. For example, **1231111111**."""


class SwishInfo2Dict(TypedDict):
    swish_number: str
