from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SvsInfo(SdkBaseModel):
    authorisation_mid: str = Field(alias="authorisationMid")
    """The merchant ID (MID) that the acquirer recognizes you by."""

    currency_code: str = Field(alias="currencyCode")
    """The three-character ISO currency code, example **USD**"""


class SvsInfoDict(TypedDict):
    authorisation_mid: str
    currency_code: str
