from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SplitDcc2(SdkBaseModel):
    """Defines the logic for booking the markup paid by the customer for Dynamic Currency Conversion (DCC).

    > This field is in pilot phase, and not yet available for all platforms."""

    account_holder_percentage: Optional[int] = Field(default=UNSET, alias="accountHolderPercentage")


class SplitDcc2Dict(TypedDict):
    account_holder_percentage: NotRequired[int]
