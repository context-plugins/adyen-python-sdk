from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type23 import Type23OrStr


class Doku(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    first_name: str = Field(alias="firstName")
    """The shopper's first name."""

    last_name: str = Field(alias="lastName")
    """The shopper's last name."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    shopper_email: str = Field(alias="shopperEmail")
    """The shopper's email."""

    type_: Type23OrStr = Field(alias="type")
    """**doku**"""


class DokuDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    first_name: str
    last_name: str
    sdk_data: NotRequired[str]
    shopper_email: str
    type_: Type23OrStr
