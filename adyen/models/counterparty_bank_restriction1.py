from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_identification import BankIdentification, BankIdentificationDict


class CounterpartyBankRestriction1(SdkBaseModel):
    """Contains a list of counterparty financial institutions and how they must be evaluated.

    Supported operations: **anyMatch**, **noneMatch**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[BankIdentification]] = UNSET
    """The list of counterparty bank institutions to be evaluated."""


class CounterpartyBankRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[list[BankIdentificationDict]]
