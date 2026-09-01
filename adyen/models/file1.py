from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class File1(SdkBaseModel):
    """For ``authType`` **wpa-eap** or **wpa2-eap**. The root certificate from the CA that signed the certificate of the
    RADIUS server that is part of your wireless network."""

    data: str
    """The certificate content converted to a Base64-encoded string."""

    name: str
    """The name of the certificate. Must be unique across Wi-Fi profiles."""


class File1Dict(TypedDict):
    data: str
    name: str
