from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class File4(SdkBaseModel):
    """For ``eap`` **tls**. The EAP intermediate certificate."""

    data: str
    """The certificate content converted to a Base64-encoded string."""

    name: str
    """The name of the certificate. Must be unique across Wi-Fi profiles."""


class File4Dict(TypedDict):
    data: str
    name: str
