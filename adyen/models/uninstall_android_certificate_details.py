from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type81 import Type81OrStr


class UninstallAndroidCertificateDetails(SdkBaseModel):
    certificate_id: Optional[str] = Field(default=UNSET, alias="certificateId")
    """The unique identifier of the certificate to be uninstalled."""

    type_: Optional[Type81OrStr] = Field(default=UNSET, alias="type")
    """Type of terminal action: Uninstall an Android certificate."""


class UninstallAndroidCertificateDetailsDict(TypedDict):
    certificate_id: NotRequired[str]
    type_: NotRequired[Type81OrStr]
