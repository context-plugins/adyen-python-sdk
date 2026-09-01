from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type36 import Type36OrStr


class Mbway(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    shopper_email: str = Field(alias="shopperEmail")
    telephone_number: str = Field(alias="telephoneNumber")
    type_: Optional[Type36OrStr] = Field(default=UNSET, alias="type")
    """**mbway**"""


class MbwayDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    sdk_data: NotRequired[str]
    shopper_email: str
    telephone_number: str
    type_: NotRequired[Type36OrStr]
