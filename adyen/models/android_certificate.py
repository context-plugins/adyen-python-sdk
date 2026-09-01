from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class AndroidCertificate(SdkBaseModel):
    description: Optional[str] = UNSET
    """The description that was provided when uploading the certificate."""

    extension: Optional[str] = UNSET
    """The file format of the certificate, as indicated by the file extension. For example, **.cert** or **.pem**."""

    id: str
    """The unique identifier of the certificate."""

    name: Optional[str] = UNSET
    """The file name of the certificate. For example, **mycert**."""

    not_after: Optional[RFC3339DateTime] = Field(default=UNSET, alias="notAfter")
    """The date when the certificate stops to be valid."""

    not_before: Optional[RFC3339DateTime] = Field(default=UNSET, alias="notBefore")
    """The date when the certificate starts to be valid."""

    status: Optional[str] = UNSET
    """The status of the certificate."""


class AndroidCertificateDict(TypedDict):
    description: NotRequired[str]
    extension: NotRequired[str]
    id: str
    name: NotRequired[str]
    not_after: NotRequired[RFC3339DateTime]
    not_before: NotRequired[RFC3339DateTime]
    status: NotRequired[str]
