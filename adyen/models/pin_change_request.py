from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PinChangeRequest(SdkBaseModel):
    encrypted_key: str = Field(alias="encryptedKey")
    """The symmetric session key that you encrypted with the `public key
    <https://docs.adyen.com/api-explorer/balanceplatform/2/get/publicKey>`__ that you received from Adyen."""

    encrypted_pin_block: str = Field(alias="encryptedPinBlock")
    """The encrypted `PIN block <https://www.pcisecuritystandards.org/glossary/pin-block>`__."""

    payment_instrument_id: str = Field(alias="paymentInstrumentId")
    """The unique identifier of the payment instrument, which is the card for which you are managing the PIN."""

    token: str
    """The 16-digit token that you used to generate the ``encryptedPinBlock``."""


class PinChangeRequestDict(TypedDict):
    encrypted_key: str
    encrypted_pin_block: str
    payment_instrument_id: str
    token: str
