from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RelayedAuthorisationData2(SdkBaseModel):
    """If you are using relayed authorisation, this object contains information from the relayed authorisation response
    from your server."""

    metadata: Optional[dict[str, str]] = UNSET
    """Contains key-value pairs of your references and descriptions, for example,
    ``customId``:``your-own-custom-field-12345``."""

    reference: Optional[str] = UNSET
    """Your reference for the relayed authorisation data."""


class RelayedAuthorisationData2Dict(TypedDict):
    metadata: NotRequired[dict[str, str]]
    reference: NotRequired[str]
