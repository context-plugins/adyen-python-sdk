from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type29 import Type29OrStr


class Voucher(SdkBaseModel):
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

    telephone_number: str = Field(alias="telephoneNumber")
    """The shopper's contact number. It must have an international number format, for example **+31 20 779 1846**.
    Formats like **+31 (0)20 779 1846** or **0031 20 779 1846** are not accepted."""

    type_: Type29OrStr = Field(alias="type")
    """**econtextvoucher**"""


class VoucherDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    first_name: str
    last_name: str
    sdk_data: NotRequired[str]
    shopper_email: str
    telephone_number: str
    type_: Type29OrStr
