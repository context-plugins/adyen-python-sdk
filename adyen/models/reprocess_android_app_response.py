from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReprocessAndroidAppResponse(SdkBaseModel):
    message: Optional[str] = Field(default=UNSET, alias="Message")
    """The result of the reprocess."""


class ReprocessAndroidAppResponseDict(TypedDict):
    message: NotRequired[str]
