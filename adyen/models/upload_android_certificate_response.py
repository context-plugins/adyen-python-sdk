from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UploadAndroidCertificateResponse(SdkBaseModel):
    id: Optional[str] = UNSET
    """The unique identifier of the uploaded Android certificate."""


class UploadAndroidCertificateResponseDict(TypedDict):
    id: NotRequired[str]
