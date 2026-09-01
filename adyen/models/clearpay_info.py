from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClearpayInfo(SdkBaseModel):
    support_url: str = Field(alias="supportUrl")
    """Support Url"""


class ClearpayInfoDict(TypedDict):
    support_url: str
