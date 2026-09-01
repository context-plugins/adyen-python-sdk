from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .android_certificate import AndroidCertificate, AndroidCertificateDict


class AndroidCertificatesResponse(SdkBaseModel):
    data: Optional[list[AndroidCertificate]] = UNSET
    """Uploaded Android certificates for Android payment terminals."""


class AndroidCertificatesResponseDict(TypedDict):
    data: NotRequired[list[AndroidCertificate | AndroidCertificateDict]]
