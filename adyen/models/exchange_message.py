from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExchangeMessage(SdkBaseModel):
    message_code: Optional[str] = Field(default=UNSET, alias="messageCode")
    message_description: Optional[str] = Field(default=UNSET, alias="messageDescription")


class ExchangeMessageDict(TypedDict):
    message_code: NotRequired[str]
    message_description: NotRequired[str]
