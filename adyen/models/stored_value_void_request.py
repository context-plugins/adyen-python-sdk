from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StoredValueVoidRequest(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    original_reference: str = Field(alias="originalReference")
    """The original pspReference of the payment to modify."""

    reference: Optional[str] = UNSET
    """Your reference for the payment modification. This reference is visible in Customer Area and in reports. Maximum
    length: 80 characters."""

    store: Optional[str] = UNSET
    """The physical store, for which this payment is processed."""

    tender_reference: Optional[str] = Field(default=UNSET, alias="tenderReference")
    """The reference of the tender."""

    unique_terminal_id: Optional[str] = Field(default=UNSET, alias="uniqueTerminalId")
    """The unique ID of a POS terminal."""


class StoredValueVoidRequestDict(TypedDict):
    merchant_account: str
    original_reference: str
    reference: NotRequired[str]
    store: NotRequired[str]
    tender_reference: NotRequired[str]
    unique_terminal_id: NotRequired[str]
