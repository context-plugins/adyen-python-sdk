from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict


class PermitRestriction(SdkBaseModel):
    max_amount: Optional[Amount] = Field(default=UNSET, alias="maxAmount")
    """The total sum amount of one or more payments made using this permit may not exceed this amount if set."""

    single_transaction_limit: Optional[Amount] = Field(default=UNSET, alias="singleTransactionLimit")
    """The amount of any single payment using this permit may not exceed this amount if set."""

    single_use: Optional[bool] = Field(default=UNSET, alias="singleUse")
    """Only a single payment can be made using this permit if set to true, otherwise multiple payments are allowed."""


class PermitRestrictionDict(TypedDict):
    max_amount: NotRequired[AmountDict]
    single_transaction_limit: NotRequired[AmountDict]
    single_use: NotRequired[bool]
