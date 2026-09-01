from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class BalanceTransferResponse(SdkBaseModel):
    created_at: RFC3339DateTime = Field(alias="createdAt")
    """The date when the balance transfer was performed."""

    psp_reference: str = Field(alias="pspReference")
    """Adyen's 16-character string reference associated with the balance transfer."""


class BalanceTransferResponseDict(TypedDict):
    created_at: RFC3339DateTime
    psp_reference: str
