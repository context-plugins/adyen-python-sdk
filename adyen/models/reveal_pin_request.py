from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RevealPinRequest(SdkBaseModel):
    encrypted_key: str = Field(alias="encryptedKey")
    """The symmetric session key that you encrypted with the `public key
    <https://docs.adyen.com/api-explorer/balanceplatform/2/get/publicKey>`__ that you received from Adyen."""

    payment_instrument_id: str = Field(alias="paymentInstrumentId")
    """The unique identifier of the payment instrument, which is the card for which you are managing the PIN."""


class RevealPinRequestDict(TypedDict):
    encrypted_key: str
    payment_instrument_id: str
