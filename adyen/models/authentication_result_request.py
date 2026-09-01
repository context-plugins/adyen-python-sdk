from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AuthenticationResultRequest(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which the authentication was processed."""

    psp_reference: str = Field(alias="pspReference")
    """The pspReference identifier for the transaction."""


class AuthenticationResultRequestDict(TypedDict):
    merchant_account: str
    psp_reference: str
