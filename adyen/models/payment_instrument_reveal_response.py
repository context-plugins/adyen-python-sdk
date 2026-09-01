from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PaymentInstrumentRevealResponse(SdkBaseModel):
    encrypted_data: str = Field(alias="encryptedData")
    """The data encrypted using the ``encryptedKey``."""


class PaymentInstrumentRevealResponseDict(TypedDict):
    encrypted_data: str
