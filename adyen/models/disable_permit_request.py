from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DisablePermitRequest(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    token: str
    """The permit token to disable."""


class DisablePermitRequestDict(TypedDict):
    merchant_account: str
    token: str
