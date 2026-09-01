from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Signature(SdkBaseModel):
    ask_signature_on_screen: Optional[bool] = Field(default=UNSET, alias="askSignatureOnScreen")
    """If ``skipSignature`` is false, indicates whether the shopper should provide a signature on the display (**true**)
    or on the merchant receipt (**false**)."""

    device_name: Optional[str] = Field(default=UNSET, alias="deviceName")
    """Name that identifies the terminal."""

    device_slogan: Optional[str] = Field(default=UNSET, alias="deviceSlogan")
    """Slogan shown on the start screen of the device."""

    skip_signature: Optional[bool] = Field(default=UNSET, alias="skipSignature")
    """Skip asking for a signature. This is possible because all global card schemes (American Express, Diners,
    Discover, JCB, MasterCard, VISA, and UnionPay) regard a signature as optional."""


class SignatureDict(TypedDict):
    ask_signature_on_screen: NotRequired[bool]
    device_name: NotRequired[str]
    device_slogan: NotRequired[str]
    skip_signature: NotRequired[bool]
