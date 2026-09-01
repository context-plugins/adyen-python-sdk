from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AffirmResponseInfo1(SdkBaseModel):
    """*affirm** details"""

    public_api_key: Optional[str] = Field(default=UNSET, alias="publicApiKey")
    """Affirm public API key"""


class AffirmResponseInfo1Dict(TypedDict):
    public_api_key: NotRequired[str]
