from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResponseAdditionalDataNetworkTokens(SdkBaseModel):
    network_token_available: Optional[str] = Field(default=UNSET, alias="networkToken.available")
    """Indicates whether a network token is available for the specified card."""

    network_token_bin: Optional[str] = Field(default=UNSET, alias="networkToken.bin")
    """The Bank Identification Number of a tokenized card, which is the first six digits of a card number."""

    network_token_token_summary: Optional[str] = Field(default=UNSET, alias="networkToken.tokenSummary")
    """The last four digits of a network token."""


class ResponseAdditionalDataNetworkTokensDict(TypedDict):
    network_token_available: NotRequired[str]
    network_token_bin: NotRequired[str]
    network_token_token_summary: NotRequired[str]
