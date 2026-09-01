from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SplitDcc(SdkBaseModel):
    account_holder_percentage: Optional[int] = Field(default=UNSET, alias="accountHolderPercentage")


class SplitDccDict(TypedDict):
    account_holder_percentage: NotRequired[int]
