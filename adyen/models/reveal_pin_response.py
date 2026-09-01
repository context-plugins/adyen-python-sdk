from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RevealPinResponse(SdkBaseModel):
    encrypted_pin_block: str = Field(alias="encryptedPinBlock")
    """The encrypted `PIN block <https://www.pcisecuritystandards.org/glossary/pin-block>`__."""

    token: str
    """The 16-digit token that you need to extract the ``encryptedPinBlock``."""


class RevealPinResponseDict(TypedDict):
    encrypted_pin_block: str
    token: str
