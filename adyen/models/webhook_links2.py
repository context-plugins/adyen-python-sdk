from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links_element6 import LinksElement6, LinksElement6Dict
from .links_element15 import LinksElement15, LinksElement15Dict
from .links_element16 import LinksElement16, LinksElement16Dict
from .links_element17 import LinksElement17, LinksElement17Dict
from .links_element19 import LinksElement19, LinksElement19Dict


class WebhookLinks2(SdkBaseModel):
    """References to resources connected with this webhook."""

    company: Optional[LinksElement15] = UNSET
    """The company account that the webhook is configured for. Only present for company-level webhooks."""

    generate_hmac: LinksElement16 = Field(alias="generateHmac")
    """Generate an HMAC key."""

    merchant: Optional[LinksElement17] = UNSET
    """The merchant account that the webhook is configured for. Only present for merchant-level webhooks."""

    self: LinksElement6
    """Link to the resource itself."""

    test_webhook: LinksElement19 = Field(alias="testWebhook")
    """Test the webhook setup."""


class WebhookLinks2Dict(TypedDict):
    company: NotRequired[LinksElement15 | LinksElement15Dict]
    generate_hmac: LinksElement16 | LinksElement16Dict
    merchant: NotRequired[LinksElement17 | LinksElement17Dict]
    self: LinksElement6 | LinksElement6Dict
    test_webhook: LinksElement19 | LinksElement19Dict
