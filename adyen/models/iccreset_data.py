from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IccresetData(SdkBaseModel):
    atr_value: Optional[str] = Field(default=UNSET, alias="ATRValue")
    card_status_words: Optional[str] = Field(default=UNSET, alias="CardStatusWords")


class IccresetDataDict(TypedDict):
    atr_value: NotRequired[str]
    card_status_words: NotRequired[str]
