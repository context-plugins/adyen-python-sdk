from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PublicKeyResponse(SdkBaseModel):
    public_key: str = Field(alias="publicKey")
    """The public key you need for encrypting a symmetric session key."""

    public_key_expiry_date: str = Field(alias="publicKeyExpiryDate")
    """The expiry date of the public key."""


class PublicKeyResponseDict(TypedDict):
    public_key: str
    public_key_expiry_date: str
