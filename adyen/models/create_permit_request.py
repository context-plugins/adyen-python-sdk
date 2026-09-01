from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .permit import Permit, PermitDict


class CreatePermitRequest(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    permits: list[Permit]
    """The permits to create for this recurring contract."""

    recurring_detail_reference: str = Field(alias="recurringDetailReference")
    """The recurring contract the new permits will use."""

    shopper_reference: str = Field(alias="shopperReference")
    """The shopper's reference to uniquely identify this shopper (e.g. user ID or account ID)."""


class CreatePermitRequestDict(TypedDict):
    merchant_account: str
    permits: list[Permit | PermitDict]
    recurring_detail_reference: str
    shopper_reference: str
