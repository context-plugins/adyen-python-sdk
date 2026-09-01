from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AndroidAppError(SdkBaseModel):
    error_code: Optional[str] = Field(default=UNSET, alias="errorCode")
    """The error code of the Android app with the ``status`` of either **error** or **invalid**."""

    terminal_models: Optional[list[str]] = Field(default=UNSET, alias="terminalModels")
    """The list of payment terminal models to which the returned ``errorCode`` applies."""


class AndroidAppErrorDict(TypedDict):
    error_code: NotRequired[str]
    terminal_models: NotRequired[list[str]]
