from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SecurityTrailer(SdkBaseModel):
    """It contains information related to the security of the message. SecurityTrailer as used by Adyen."""

    adyen_crypto_version: int = Field(alias="AdyenCryptoVersion")
    key_identifier: str = Field(alias="KeyIdentifier")
    key_version: int = Field(alias="KeyVersion")
    nonce: str = Field(alias="Nonce")
    hmac: str = Field(alias="Hmac")


class SecurityTrailerDict(TypedDict):
    adyen_crypto_version: int
    key_identifier: str
    key_version: int
    nonce: str
    hmac: str
