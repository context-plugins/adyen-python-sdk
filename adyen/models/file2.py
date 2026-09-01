from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class File2(SdkBaseModel):
    """For ``eap`` **tls**. The certificate chain for the terminals. All terminals in the same network will use the same
    EAP client certificate."""

    data: str
    """The certificate content converted to a Base64-encoded string."""

    name: str
    """The name of the certificate. Must be unique across Wi-Fi profiles."""


class File2Dict(TypedDict):
    data: str
    name: str
