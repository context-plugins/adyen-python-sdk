from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClearpayResponseInfo1(SdkBaseModel):
    """**clearpay** details"""

    support_url: Optional[str] = Field(default=UNSET, alias="supportUrl")
    """Support Url"""


class ClearpayResponseInfo1Dict(TypedDict):
    support_url: NotRequired[str]
