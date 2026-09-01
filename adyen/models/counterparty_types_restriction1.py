from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.value import ValueOrStr


class CounterpartyTypesRestriction1(SdkBaseModel):
    """Contains a list of counterparty types and how they must be evaluated.

    Supported operations: **anyMatch**, **noneMatch**.

    Supported value inputs:
    - **balanceAccount**
    - **bankAccount**
    - **card**
    - **transferInstrument**"""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[ValueOrStr]] = UNSET
    """The list of counterparty types to be evaluated."""


class CounterpartyTypesRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[list[ValueOrStr]]
