from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type17 import Type17, Type17OrStr


class Cellulant(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    issuer: Optional[str] = UNSET
    """The Cellulant issuer."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    type_: Type17OrStr = Field(default=Type17.CELLULANT, alias="type")
    """**Cellulant**"""


class CellulantDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    issuer: NotRequired[str]
    sdk_data: NotRequired[str]
    type_: NotRequired[Type17OrStr]
