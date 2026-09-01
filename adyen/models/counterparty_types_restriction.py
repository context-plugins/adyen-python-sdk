from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.value import ValueOrStr


class CounterpartyTypesRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[ValueOrStr]] = UNSET
    """The list of counterparty types to be evaluated."""


class CounterpartyTypesRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[list[ValueOrStr]]
