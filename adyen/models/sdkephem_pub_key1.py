from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SdkephemPubKey1(SdkBaseModel):
    """The ``sdkEphemPubKey`` value as received from the 3D Secure 2 SDK."""

    crv: Optional[str] = UNSET
    """The ``crv`` value as received from the 3D Secure 2 SDK."""

    kty: Optional[str] = UNSET
    """The ``kty`` value as received from the 3D Secure 2 SDK."""

    x: Optional[str] = UNSET
    """The ``x`` value as received from the 3D Secure 2 SDK."""

    y: Optional[str] = UNSET
    """The ``y`` value as received from the 3D Secure 2 SDK."""


class SdkephemPubKey1Dict(TypedDict):
    crv: NotRequired[str]
    kty: NotRequired[str]
    x: NotRequired[str]
    y: NotRequired[str]
