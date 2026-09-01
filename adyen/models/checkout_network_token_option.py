from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CheckoutNetworkTokenOption(SdkBaseModel):
    include_cryptogram: Optional[bool] = Field(default=UNSET, alias="includeCryptogram")
    """Set to **true** to enable forwarding network token cryptograms."""

    use_network_token: Optional[bool] = Field(default=UNSET, alias="useNetworkToken")
    """Set to **true** to forward the network token for a card."""


class CheckoutNetworkTokenOptionDict(TypedDict):
    include_cryptogram: NotRequired[bool]
    use_network_token: NotRequired[bool]
