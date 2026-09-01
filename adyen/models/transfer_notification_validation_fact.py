from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferNotificationValidationFact(SdkBaseModel):
    result: Optional[str] = UNSET
    """The evaluation result of the validation fact."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of the validation fact."""


class TransferNotificationValidationFactDict(TypedDict):
    result: NotRequired[str]
    type_: NotRequired[str]
