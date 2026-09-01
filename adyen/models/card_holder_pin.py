from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pinformat1 import Pinformat1OrStr


class CardHolderPin(SdkBaseModel):
    encr_pin_block: str = Field(alias="EncrPINBlock")
    pin_format: Pinformat1OrStr = Field(alias="PINFormat")
    """Possible values:
    * **ISO0**
    * **ISO1**
    * **ISO2**
    * **ISO3**"""

    additional_input: Optional[str] = Field(default=UNSET, alias="AdditionalInput")


class CardHolderPinDict(TypedDict):
    encr_pin_block: str
    pin_format: Pinformat1OrStr
    additional_input: NotRequired[str]
