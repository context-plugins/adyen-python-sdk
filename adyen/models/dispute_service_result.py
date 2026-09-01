from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DisputeServiceResult(SdkBaseModel):
    error_message: Optional[str] = Field(default=UNSET, alias="errorMessage")
    """The general error message."""

    success: bool
    """Indicates whether the request succeeded."""


class DisputeServiceResultDict(TypedDict):
    error_message: NotRequired[str]
    success: bool
