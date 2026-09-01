from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UtilityResponse(SdkBaseModel):
    origin_keys: Optional[dict[str, str]] = Field(default=UNSET, alias="originKeys")
    """The list of origin keys for all requested domains. For each list item, the key is the domain and the value is the
    origin key."""


class UtilityResponseDict(TypedDict):
    origin_keys: NotRequired[dict[str, str]]
