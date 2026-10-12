from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_identification import BankIdentification, BankIdentificationDict


class CounterpartyBankRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[BankIdentification]] = UNSET
    """The list of counterparty bank institutions to be evaluated."""


class CounterpartyBankRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[list[BankIdentificationDict]]
