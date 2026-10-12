from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .stored_value_account_id import StoredValueAccountId, StoredValueAccountIdDict


class StoredValueAccountStatus(SdkBaseModel):
    stored_value_account_id: StoredValueAccountId = Field(alias="StoredValueAccountID")
    """Identification of the stored value account or the stored value card and the associated product sold by the Sale
    System for stored value requests."""

    current_balance: Optional[float] = Field(default=UNSET, alias="CurrentBalance")
    """If relevant and known."""


class StoredValueAccountStatusDict(TypedDict):
    stored_value_account_id: StoredValueAccountIdDict
    current_balance: NotRequired[float]
