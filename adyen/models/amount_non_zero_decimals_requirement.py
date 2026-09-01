from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AmountNonZeroDecimalsRequirement(SdkBaseModel):
    description: Optional[str] = UNSET
    """Specifies for which routes the amount in a transfer request must have no non-zero decimal places, so the transfer
    can only be processed if the amount consists of round numbers."""

    type_: Literal["amountNonZeroDecimalsRequirement"] = Field(default="amountNonZeroDecimalsRequirement", alias="type")
    """**amountNonZeroDecimalsRequirement**"""


class AmountNonZeroDecimalsRequirementDict(TypedDict):
    description: NotRequired[str]
    type_: NotRequired[Literal["amountNonZeroDecimalsRequirement"]]
