from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class File3(SdkBaseModel):
    """For ``eap`` **tls**. The RSA private key for the client. Include the lines BEGIN RSA PRIVATE KEY and END RSA
    PRIVATE KEY."""

    data: str
    """The certificate content converted to a Base64-encoded string."""

    name: str
    """The name of the certificate. Must be unique across Wi-Fi profiles."""


class File3Dict(TypedDict):
    data: str
    name: str
