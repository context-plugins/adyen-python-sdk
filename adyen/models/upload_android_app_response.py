from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UploadAndroidAppResponse(SdkBaseModel):
    id: Optional[str] = UNSET
    """The unique identifier of the uploaded Android app."""


class UploadAndroidAppResponseDict(TypedDict):
    id: NotRequired[str]
