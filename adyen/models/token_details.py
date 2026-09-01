from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TokenDetails(SdkBaseModel):
    token_data: Optional[dict[str, str]] = Field(default=UNSET, alias="tokenData")
    token_data_type: Optional[str] = Field(default=UNSET, alias="tokenDataType")


class TokenDetailsDict(TypedDict):
    token_data: NotRequired[dict[str, str]]
    token_data_type: NotRequired[str]
