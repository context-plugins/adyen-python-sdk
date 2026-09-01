from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ThreeDs2ResultRequest(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    psp_reference: str = Field(alias="pspReference")
    """The pspReference returned in the /authorise call."""


class ThreeDs2ResultRequestDict(TypedDict):
    merchant_account: str
    psp_reference: str
