from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type42 import Type42, Type42OrStr


class InstallAndroidCertificateDetails(SdkBaseModel):
    certificate_id: Optional[str] = Field(default=UNSET, alias="certificateId")
    """The unique identifier of the certificate to be installed."""

    type_: Type42OrStr = Field(default=Type42.INSTALL_ANDROID_CERTIFICATE, alias="type")
    """Type of terminal action: Install an Android certificate."""


class InstallAndroidCertificateDetailsDict(TypedDict):
    certificate_id: NotRequired[str]
    type_: NotRequired[Type42OrStr]
