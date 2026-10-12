from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links_element1 import LinksElement1, LinksElement1Dict
from .links_element2 import LinksElement2, LinksElement2Dict
from .links_element3 import LinksElement3, LinksElement3Dict
from .links_element4 import LinksElement4, LinksElement4Dict
from .links_element5 import LinksElement5, LinksElement5Dict
from .links_element6 import LinksElement6, LinksElement6Dict


class ApiCredentialLinks(SdkBaseModel):
    allowed_origins: Optional[LinksElement1] = Field(default=UNSET, alias="allowedOrigins")
    """List of allowed origins."""

    company: Optional[LinksElement2] = UNSET
    """Company account that the API credential is linked to. Only present for company-level webhooks."""

    generate_api_key: Optional[LinksElement3] = Field(default=UNSET, alias="generateApiKey")
    """Generates a new API key. When you generate a new one, the existing key remains valid for 24 hours."""

    generate_client_key: Optional[LinksElement4] = Field(default=UNSET, alias="generateClientKey")
    """Generates a new client key, used to authenticate client-side requests. When you generate a new one, the existing
    key remains valid for 24 hours."""

    merchant: Optional[LinksElement5] = UNSET
    """The merchant account that the API credential is linked to. Only present for merchant-level API credentials."""

    self: LinksElement6
    """Link to the resource itself."""


class ApiCredentialLinksDict(TypedDict):
    allowed_origins: NotRequired[LinksElement1Dict]
    company: NotRequired[LinksElement2Dict]
    generate_api_key: NotRequired[LinksElement3Dict]
    generate_client_key: NotRequired[LinksElement4Dict]
    merchant: NotRequired[LinksElement5Dict]
    self: LinksElement6Dict
