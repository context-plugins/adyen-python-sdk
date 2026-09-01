from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PermitResult(SdkBaseModel):
    result_key: Optional[str] = Field(default=UNSET, alias="resultKey")
    """The key to link permit requests to permit results."""

    token: Optional[str] = UNSET
    """The permit token which is used to make payments by the partner company."""


class PermitResultDict(TypedDict):
    result_key: NotRequired[str]
    token: NotRequired[str]
