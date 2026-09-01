from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BinDetail(SdkBaseModel):
    issuer_country: Optional[str] = Field(default=UNSET, alias="issuerCountry")
    """The country where the card was issued."""


class BinDetailDict(TypedDict):
    issuer_country: NotRequired[str]
