from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SvsResponseInfo2(SdkBaseModel):
    """**svs** details"""

    authorisation_mid: Optional[str] = Field(default=UNSET, alias="authorisationMid")
    """The merchant ID (MID) that the acquirer recognizes you by."""

    currency_code: Optional[str] = Field(default=UNSET, alias="currencyCode")
    """The three-character ISO currency code, example **USD**"""


class SvsResponseInfo2Dict(TypedDict):
    authorisation_mid: NotRequired[str]
    currency_code: NotRequired[str]
