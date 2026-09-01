from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DspublicKeyDetail(SdkBaseModel):
    brand: Optional[str] = UNSET
    """Card brand."""

    directory_server_id: Optional[str] = Field(default=UNSET, alias="directoryServerId")
    """Directory Server (DS) identifier."""

    from_sdk_version: Optional[str] = Field(default=UNSET, alias="fromSDKVersion")
    """The version of the mobile 3D Secure 2 SDK. For the possible values, refer to the versions in `Adyen 3DS2 Android
    <https://github.com/Adyen/adyen-3ds2-android/releases>`__ and `Adyen 3DS2 iOS
    <https://github.com/Adyen/adyen-3ds2-ios/releases>`__."""

    public_key: Optional[str] = Field(default=UNSET, alias="publicKey")
    """Public key. The 3D Secure 2 SDK encrypts the device information by using the DS public key."""

    root_certificates: Optional[str] = Field(default=UNSET, alias="rootCertificates")
    """Directory Server root certificates. The 3D Secure 2 SDK verifies the ACS signed content using the
    rootCertificates."""


class DspublicKeyDetailDict(TypedDict):
    brand: NotRequired[str]
    directory_server_id: NotRequired[str]
    from_sdk_version: NotRequired[str]
    public_key: NotRequired[str]
    root_certificates: NotRequired[str]
