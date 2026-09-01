from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.plan1 import Plan1OrStr


class InstallmentOption(SdkBaseModel):
    max_value: Optional[int] = Field(default=UNSET, alias="maxValue")
    """The maximum number of installments offered for this payment method."""

    plans: Optional[list[Plan1OrStr]] = UNSET
    """Defines the type of installment plan. If not set, defaults to **regular**.

    Possible values:
    * **regular**
    * **revolving**"""

    preselected_value: Optional[int] = Field(default=UNSET, alias="preselectedValue")
    """Preselected number of installments offered for this payment method."""

    values: Optional[list[int]] = UNSET
    """An array of the number of installments that the shopper can choose from. For example, **[2,3,5]**. This cannot be
    specified simultaneously with ``maxValue``."""


class InstallmentOptionDict(TypedDict):
    max_value: NotRequired[int]
    plans: NotRequired[list[Plan1OrStr]]
    preselected_value: NotRequired[int]
    values: NotRequired[list[int]]
